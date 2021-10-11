from fastapi import HTTPException, Depends, Path, status

from app.models.doctor import DoctorPublicFriendly

from app.db.repositories.doctors import DoctorsRepository

from app.api.dependencies.database import get_repository

async def get_doctor_by_id_from_path(
    doctor_id: int = Path(..., ge=1),
    doctors_repo: DoctorsRepository = Depends(get_repository(DoctorsRepository)),
) -> DoctorPublicFriendly:
    doctor = await doctors_repo.get_doctor_by_id(id=doctor_id)
    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No doctor found with that id.",
        )

    return doctor
