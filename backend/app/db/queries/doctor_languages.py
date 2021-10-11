CREATE_DOCTOR_LANGUAGES_QUERY = "INSERT INTO doctor_languages (doctor_id, language_id) VALUES (:doctor_id, :language_id)"

GET_LANGUAGES_BY_DOCTOR_ID = """
    SELECT lang FROM doctor_languages 
    INNER JOIN languages ON doctor_languages.language_id = languages.id 
    WHERE doctor_languages.doctor_id = :doctor_id;
"""