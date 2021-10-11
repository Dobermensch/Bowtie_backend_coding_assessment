from typing import Set, Optional
# from enum import Enum
from app.models.core import IDModelMixin, CoreModel

# Base - all shared attributes of a resource
# Create - attributes required to create a new resource - used at POST requests
# Update - attributes that can be updated - used at PUT requests
# InDB - attributes present on any resource coming out of the database
# Public - attributes present on public facing resources being returned from GET, POST, and PUT requests

class DoctorBase(CoreModel):
    """
    All common characteristics of our Doctor resource
    """
    first_name: str
    last_name: Optional[str]
    full_name: str
    address: str
    area: int
    opening_hours: str
    price: str

class DoctorCreate(DoctorBase):
    services: Set[int] = set()
    languages: Set[int] = set()

class DoctorUpdate(DoctorBase):
    pass

class DoctorInDB(IDModelMixin, DoctorBase):
    pass

class DoctorPublic(IDModelMixin, DoctorCreate):
    pass

class DoctorPublicFriendly(IDModelMixin, DoctorCreate):
    services: Set[str] = set()
    languages: Set[str] = set()
    area: str