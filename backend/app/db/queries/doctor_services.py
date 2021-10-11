CREATE_DOCTOR_SERVICES_QUERY = "INSERT INTO doctor_services (doctor_id, service_id) VALUES (:doctor_id, :service_id)"

GET_SERVICES_BY_DOCTOR_ID = """
    SELECT type FROM doctor_services
    INNER JOIN services on doctor_services.service_id = services.id
    WHERE doctor_id = :doctor_id;
"""