
from typing import List, Optional
from fastapi import APIRouter

from fastapi import APIRouter, Body, Depends  
from starlette.status import HTTP_201_CREATED  

from app.models.doctor import DoctorCreate, DoctorPublic, DoctorPublicFriendly
from app.db.repositories.doctors import DoctorsRepository
from app.models.doctor_languages import DoctorLanguagesCreate
from app.api.dependencies.database import get_repository

from app.api.dependencies.doctors import get_doctor_by_id_from_path

router = APIRouter()

@router.get("/", response_model=List[DoctorPublic], name="doctors:get-all-doctors")
async def get_all_doctors(
    district: Optional[str] = None,
    category: Optional[str] = None,
    pricerange: Optional[str] = None,
    language: Optional[str] = None,
    doctors_repo: DoctorsRepository = Depends(get_repository(DoctorsRepository))
) -> List[dict]:
    return await doctors_repo.list_all_doctors(district=district,category=category,pricerange=pricerange,language=language) 

@router.post("/", response_model=DoctorPublic, name="doctors:create-doctor", status_code=HTTP_201_CREATED)
async def create_new_doctor(
    new_doctor: DoctorCreate = Body(..., embed=True),
    doctors_repo: DoctorsRepository = Depends(get_repository(DoctorsRepository))
) -> DoctorPublic:
    return await doctors_repo.create_doctor(new_doctor=new_doctor)


@router.get("/{doctor_id}/", response_model=DoctorPublicFriendly, name="doctors:get-doctor-by-id")
async def get_doctor_by_id(doctor: DoctorPublicFriendly = Depends(get_doctor_by_id_from_path)) -> DoctorPublicFriendly:
    return doctor