# The purpose of a repository is to serve as a layer of abstraction on top of database actions. 
# Each repository encapsulates database functionality corresponding to a particular resource.
# In doing so, we decouple persistence logic from our application logic

# One of the benefits of using the Repository pattern is that we get the flexibility of pure SQL, 
# with the clean interface of an ORM.
from typing import List, Optional


from app.db.repositories.base import BaseRepository
from app.models.doctor import DoctorBase, DoctorCreate, DoctorPublic, DoctorPublicFriendly
from app.models.doctor_languages import DoctorLanguagesInDB
from app.db.queries.doctors import CREATE_DOCTOR_QUERY, GET_DOCTOR_BY_ID_QUERY, GET_ALL_DOCTORS_IDS, GET_DOCTORS_IDS_BY_AREA, GET_DOCTOR_IDS_BY_CATEGORY, GET_DOCTORS_IDS_WITHIN_PRICERANGE, GET_DOCTOR_IDS_BY_LANGUAGE, GET_DOCTORS_BY_IDS
from app.db.queries.doctor_languages import CREATE_DOCTOR_LANGUAGES_QUERY, GET_LANGUAGES_BY_DOCTOR_ID
from app.db.queries.doctor_services import CREATE_DOCTOR_SERVICES_QUERY, GET_SERVICES_BY_DOCTOR_ID
from app.db.queries.areas import GET_AREA_BY_ID, GET_AREA_BY_NAME

class DoctorsRepository(BaseRepository):
    """"
    All database actions associated with the Doctor resource
    """

    async def create_doctor(self, *, new_doctor: DoctorCreate) -> DoctorPublic:
        create_doctor_query_values = new_doctor.dict(exclude={"services", "languages"})
        
        async with self.db.transaction():
            created_doctor = await self.db.fetch_one(query=CREATE_DOCTOR_QUERY, values=create_doctor_query_values)

            created_doctor = DoctorPublic(**created_doctor)

            await self.db.execute_many(CREATE_DOCTOR_LANGUAGES_QUERY,
            [{"doctor_id": created_doctor.id, "language_id": language_id} for language_id in new_doctor.languages])

            created_doctor.languages = new_doctor.languages

            await self.db.execute_many(CREATE_DOCTOR_SERVICES_QUERY,
            [{"doctor_id": created_doctor.id, "service_id": service_id} for service_id in new_doctor.services])

            created_doctor.services = new_doctor.services

        return created_doctor

    async def get_doctor_by_id(self, *, id: int) -> DoctorPublicFriendly:
        async with self.db.transaction():
            doctor = await self.db.fetch_one(query=GET_DOCTOR_BY_ID_QUERY, values={"id": id})
            if not doctor:
                return None

            doctor = DoctorPublicFriendly(**doctor)

            doctor_langs = await self.db.fetch_all(query=GET_LANGUAGES_BY_DOCTOR_ID, values={"doctor_id": id})
            doctor.languages = [r["lang"] for r in doctor_langs]

            doctor_services = await self.db.fetch_all(query=GET_SERVICES_BY_DOCTOR_ID, values={"doctor_id": id})
            doctor.services = [r["type"] for r in doctor_services]

            area = await self.db.fetch_one(query=GET_AREA_BY_ID, values={"id": int(doctor.area)})
            doctor.area = area["name"]

        return doctor

    
    async def list_all_doctors(
            self, 
            district: Optional[str] = None,
            category: Optional[str] = None, 
            pricerange: Optional[str] = None, 
            language: Optional[str] = None
        ) -> List[DoctorPublic]:
        all_doctors = await self.db.fetch_all(query=GET_ALL_DOCTORS_IDS)

        if district is not None:
            area = await self.db.fetch_one(query=GET_AREA_BY_NAME, values={"name": district})

            if area is None:
                return None
            
            all_doctors = await self.db.fetch_all(query=GET_DOCTORS_IDS_BY_AREA, values={"area_id": area["id"]})

        if category is not None:
            all_doctors = [d["id"] for d in all_doctors]
            all_doctors = await self.db.fetch_all(query=GET_DOCTOR_IDS_BY_CATEGORY, values={"doctor_ids": all_doctors, "category": category})
        
        if pricerange is not None:
            split_range = pricerange.split("-")
            minimum = split_range[0]
            maximum = split_range[1]
            all_doctors = [d["id"] for d in all_doctors]

            all_doctors = await self.db.fetch_all(query=GET_DOCTORS_IDS_WITHIN_PRICERANGE, values={"doctor_ids": all_doctors, "minimum": minimum, "maximum": maximum})

        if language is not None:
            all_doctors = [d["id"] for d in all_doctors]
            all_doctors = await self.db.fetch_all(query=GET_DOCTOR_IDS_BY_LANGUAGE, values={"doctor_ids": all_doctors, "language": language})

        all_doctors = [d["id"] for d in all_doctors]
        all_doctors = await self.db.fetch_all(query=GET_DOCTORS_BY_IDS, values={"doctor_ids": all_doctors})

        # TODO: add services and languages to response

        return [DoctorPublic(**d) for d in all_doctors]
