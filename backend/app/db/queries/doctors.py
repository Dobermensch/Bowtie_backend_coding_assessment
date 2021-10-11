CREATE_DOCTOR_QUERY = """
    INSERT INTO doctors (first_name, last_name, full_name, address, area, opening_hours, price)
    VALUES (:first_name, :last_name, :full_name, :address, :area, :opening_hours, :price)
    RETURNING id, first_name, last_name, full_name, address, area, opening_hours, price;
"""

GET_DOCTOR_BY_ID_QUERY = """
    SELECT * FROM doctors where doctors.id = :id;
"""

GET_ALL_DOCTORS_IDS = "SELECT id FROM doctors;"

GET_DOCTORS_IDS_BY_AREA = "SELECT id FROM doctors WHERE doctors.area = :area_id;"

GET_DOCTOR_IDS_BY_CATEGORY = """
    SELECT doctor_services.doctor_id AS id from doctor_services 
    INNER JOIN services ON doctor_services.service_id = services.id
    WHERE services.type = :category AND doctor_services.doctor_id = ANY(:doctor_ids);
"""

GET_DOCTORS_IDS_WITHIN_PRICERANGE = """
    SELECT id FROM doctors WHERE price -> 'fee' >= :minimum AND price -> 'fee' <= :maximum AND id = ANY(:doctor_ids);
"""

GET_DOCTOR_IDS_BY_LANGUAGE = """
    SELECT doctor_languages.doctor_id AS id FROM doctor_languages
    INNER JOIN languages ON doctor_languages.language_id = languages.id
    WHERE doctor_languages.doctor_id = ANY(:doctor_ids) AND languages.lang = :language;
"""

GET_DOCTORS_BY_IDS = "SELECT * FROM doctors WHERE id = ANY(:doctor_ids);"