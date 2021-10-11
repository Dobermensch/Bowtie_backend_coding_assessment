import pytest
import json
from typing import List

from httpx import AsyncClient
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from app.models.doctor import DoctorCreate, DoctorPublic, DoctorPublicFriendly

# decorate all tests with @pytest.mark.asyncio
pytestmark = pytest.mark.asyncio

@pytest.fixture
def new_doctor():
    return DoctorCreate(
        first_name="test_doc",
        last_name="test_doc",
        full_name="test_doc test_doc",
        address="test",
        area=1,
        opening_hours=json.dumps({
            "monday": {"starting": "9:00", "closing": "18:00"},
            "tuesday": {"starting": "9:00", "closing": "18:00"},
            "wednesday": {"starting": "9:00", "closing": "18:00"},
            "thursday": {"starting": "9:00", "closing": "18:00"},
            "friday": {"starting": "9:00", "closing": "18:00"},
            "saturday": {"starting": "9:00", "closing": "18:00"},
            "sunday": {"starting": "9:00", "closing": "18:00"},
            "public_holidays": {},
        }),
        price=json.dumps({
            "fee": 100,
            "western_inclusive": False,
            "days_inclusive": "",
            "currency": "HKD"
        }),
        service=[1],
        languages=[1,2]
    )

class TestDoctorsRoutes:
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("doctors:create-doctor"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND

    async def test_invalid_input_raises_error(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("doctors:create-doctor"), json={})
        assert res.status_code == HTTP_422_UNPROCESSABLE_ENTITY

    """
    Check each cleaning route to ensure none return 404s
    """
    async def test_routes_exist(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(app.url_path_for("doctors:create-doctor"), json={})
        assert res.status_code != HTTP_404_NOT_FOUND
        res = await client.get(app.url_path_for("doctors:get-doctor-by-id", doctor_id=1))
        assert res.status_code != HTTP_404_NOT_FOUND
        res = await client.get(app.url_path_for("doctors:get-all-doctors"))
        assert res.status_code != HTTP_404_NOT_FOUND

class TestCreateDoctor:
    async def test_valid_input_creates_doctor(
        self, app: FastAPI, client: AsyncClient, new_doctor: DoctorCreate
    ) -> None:
        res = await client.post(
            app.url_path_for("doctors:create-doctor"), json={"new_doctor": jsonable_encoder(new_doctor)}
        )

        assert res.status_code == HTTP_201_CREATED
        created_doctor = DoctorPublic(**res.json()).dict()
        new_doctor_dict = new_doctor.dict()
        assert created_doctor["first_name"] == new_doctor.first_name
        assert created_doctor["last_name"] == new_doctor.last_name
        assert created_doctor["full_name"] == new_doctor.full_name
        assert created_doctor["address"] == new_doctor.address
        assert created_doctor["area"] == new_doctor.area
        # TODO: check other attributes if necessary

    
    @pytest.mark.parametrize(
        "invalid_payload, status_code",
        (
            (None, 422),
            ({}, 422),
            ({"first_name": "test_name"}, 422),
            ({"price": 10.00}, 422),
            ({"last_name": "test_name"}, 422),
        ),
    )
    async def test_invalid_input_raises_error(
        self, app: FastAPI, client: AsyncClient, invalid_payload: dict, status_code: int
    ) -> None:
        res = await client.post(
            app.url_path_for("doctors:create-doctor"), json={"new_doctor": invalid_payload}
        )
        assert res.status_code == status_code
 
class TestGetDoctor:
    async def test_get_doctor_by_id(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get(app.url_path_for("doctors:get-doctor-by-id", doctor_id=1))
        assert res.status_code == HTTP_200_OK
        doctor = DoctorPublicFriendly(**res.json())
        assert doctor.id == 1

    @pytest.mark.parametrize(
        "id, status_code", ((50000, 404), (-1, 422), (None, 422)),
    )
    async def test_wrong_id_returns_error(
        self, app: FastAPI, client: AsyncClient, id: int, status_code: int
    ) -> None:
        res = await client.get(app.url_path_for("doctors:get-doctor-by-id", doctor_id=id))
        assert res.status_code == status_code

    async def test_get_all_doctors(
        self,
        app: FastAPI,
        client: AsyncClient,
        new_doctor: DoctorCreate
    ) -> None:
        res = await client.get(app.url_path_for("doctors:get-all-doctors"))
        assert res.status_code == HTTP_200_OK
        res_json = res.json()
        assert isinstance(res_json, list)
        assert len(res_json) > 0
        # two doctors from seed and one doctor created above
        assert(len(res_json) == 3)
    
    # TODO: check for individual attributes maybe
        