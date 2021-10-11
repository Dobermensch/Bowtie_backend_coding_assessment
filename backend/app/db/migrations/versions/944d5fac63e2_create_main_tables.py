"""create_main_tables

Revision ID: 944d5fac63e2
Revises: 
Create Date: 2021-09-25 13:26:52.023083

"""
from alembic import op
import sqlalchemy as sa
import json


# revision identifiers, used by Alembic
revision = '944d5fac63e2'
down_revision = None
branch_labels = None
depends_on = None

def create_languages_table() -> None:
    lang_table = op.create_table(
        "languages",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("lang", sa.Text, nullable=False),
    )

    op.bulk_insert(
        lang_table,
        [
            {'lang':'en'},
            {'lang': 'cn-zh'}
        ]
    )

def create_area_table() -> None:
    area_table = op.create_table(
        "areas",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
    )

    op.bulk_insert(
        area_table,
        [
            {'name':'Central'},
            {'name': 'Admiralty'}
        ]
    )

opening_hours = {
    "monday": {"starting": "9:00", "closing": "18:00"},
    "tuesday": {"starting": "9:00", "closing": "18:00"},
    "wednesday": {"starting": "9:00", "closing": "18:00"},
    "thursday": {"starting": "9:00", "closing": "18:00"},
    "friday": {"starting": "9:00", "closing": "18:00"},
    "saturday": {"starting": "9:00", "closing": "18:00"},
    "sunday": {"starting": "9:00", "closing": "18:00"},
    "public_holidays": {},
}

fees = {
    "fee": 100,
    "western_inclusive": False,
    "days_inclusive": "",
    "currency": "HKD"
}

def create_doctors_table() -> None:
    doctors_table = op.create_table(
        "doctors",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("first_name", sa.Text, nullable=False),
        sa.Column("last_name", sa.Text, nullable=True),
        sa.Column("full_name", sa.Text, nullable=True),
        sa.Column("address", sa.Text, nullable=False),
        sa.Column("area", sa.Integer, sa.ForeignKey("areas.id"), nullable=False),
        sa.Column("opening_hours", sa.dialects.postgresql.JSONB, nullable=False, server_default=json.dumps(opening_hours)),
        sa.Column("price", sa.dialects.postgresql.JSONB, nullable=False, server_default=json.dumps(fees)),
    )

    op.bulk_insert(
        doctors_table,
        [
            {'first_name': 'Doctor', 'last_name': 'McDoctorFace', 'full_name': 'Doctor McDoctorFace', 'address': '420/F, Made up Commercial Building, Made up road, Central', 'area': 1},
            {'first_name': 'Boaty', 'last_name': 'McBoatFace', 'full_name': 'Boaty McBoatFace', 'address': '69/F, Made up Commercial Building 2, Made up road 2, Admiralty', 'area': 2},
        ]
    )

def create_doctor_languages_table() -> None:
    doctor_lang_table = op.create_table(
        "doctor_languages",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("doctor_id", sa.Integer, sa.ForeignKey("doctors.id"), nullable=False),
        sa.Column("language_id", sa.Integer, sa.ForeignKey("languages.id"), nullable=False),
    )

    op.bulk_insert(
        doctor_lang_table,
        [
            {'doctor_id': 1, 'language_id': 1},
            {'doctor_id': 2, 'language_id': 1}
        ]
    )

def create_services_table() -> None:
    service_table = op.create_table(
        "services",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("type", sa.Text, nullable=False)
    )

    op.bulk_insert(
        service_table,
        [
            {'type': 'surgeon'},
            {'type': 'gynecologist'}
        ]
    )

def create_doctor_services() -> None:
    doctor_services_table = op.create_table(
        "doctor_services",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("doctor_id", sa.Integer, sa.ForeignKey("doctors.id"), nullable=False),
        sa.Column("service_id", sa.Integer, sa.ForeignKey("services.id"), nullable=False)
    )

    op.bulk_insert(
        doctor_services_table,
        [
            {'doctor_id': 1, 'service_id': 1},
            {'doctor_id': 2, 'service_id': 2},
        ]
    )

def upgrade() -> None:
    create_languages_table()
    create_area_table()
    create_doctors_table()
    create_doctor_languages_table()
    create_services_table()
    create_doctor_services()


def downgrade() -> None:
    op.drop_table("areas")
    op.drop_table("doctor_languages")
    op.drop_table("doctor_services")
    op.drop_table("doctors")
    op.drop_table("languages")
    op.drop_table("services")


