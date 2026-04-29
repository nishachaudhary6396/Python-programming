import pytest
@pytest.fixture
def student_data():
    return {
        "name": "nisha",
        "course": "btech cs",
        "marks": 50
    }
def test_student_name(student_data):
    assert student_data["name"] == "nisha"

def test_student_mark(student_data):
    assert student_data["marks"] >=20

def test_add_extra_marks(student_data):
    student_data["marks"] +=10
    assert student_data["marks"] ==60