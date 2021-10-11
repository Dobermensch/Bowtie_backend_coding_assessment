from app.models.core import IDModelMixin, CoreModel

# Base - all shared attributes of a resource
# Create - attributes required to create a new resource - used at POST requests
# Update - attributes that can be updated - used at PUT requests
# InDB - attributes present on any resource coming out of the database
# Public - attributes present on public facing resources being returned from GET, POST, and PUT requests

class DoctorLanguagesBase(CoreModel):
    """
    All common characteristics of our Doctor Language resource
    """

    doctor_id: int
    language_id: int

class DoctorLanguagesCreate(DoctorLanguagesBase):
    pass

class DoctorLanguagesUpdate(DoctorLanguagesBase):
    pass

class DoctorLanguagesInDB(IDModelMixin, DoctorLanguagesBase):
    pass

class DoctorLanguagesPublic(IDModelMixin, DoctorLanguagesBase):
    pass