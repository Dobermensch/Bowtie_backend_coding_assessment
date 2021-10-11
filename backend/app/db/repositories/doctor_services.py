# The purpose of a repository is to serve as a layer of abstraction on top of database actions. 
# Each repository encapsulates database functionality corresponding to a particular resource.
# In doing so, we decouple persistence logic from our application logic

# One of the benefits of using the Repository pattern is that we get the flexibility of pure SQL, 
# with the clean interface of an ORM.

from app.db.repositories.base import BaseRepository
from app.models.doctor import DoctorCreate, DoctorUpdate, DoctorInDB

CREATE_DOCTOR_QUERY = """
    INSERT INTO doctors (first_name, last_name, full_name, address, area, opening_hours, price)
    VALUES (:first_name, :last_name, :full_name, :address, :area, :opening_hours, :price)
    RETURNING id, first_name, last_name, full_name, address, area, opening_hours, price;
"""

class DoctorsRepository(BaseRepository):
    """"
    All database actions associated with the Doctor resource
    """

    async def create_doctor(self, *, new_doctor: DoctorCreate) -> DoctorInDB:
        query_values = new_doctor.dict()
        doctor = await self.db.fetch_one(query=CREATE_DOCTOR_QUERY, values=query_values)
        
        return DoctorInDB(**doctor)

