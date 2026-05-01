import pytest
from healthcare import validate_patient, PatientValidationError

def test_valid_patient():
    assert validate_patient(25, 75) == "Valid Patient"

def test_invalid_age():
    with pytest.raises(PatientValidationError, match="Invalid age"):
        validate_patient(130, 75)

def test_invalid_heart_rate():
    with pytest.raises(PatientValidationError, match="Invalid heart rate"):
        validate_patient(25, 250)