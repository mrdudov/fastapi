import string
from typing import Optional
from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Jhon",
        "age": 17,
        "class": "year 12"
    }
}

@app.get('/')
def index():
    return {
        "name": "First Data"
    }

@app.get("/get-student/{student_id}")
def get_student(student_id: int =  Path(None, description="The ID of the student", gt=0, lt=3)):
    """
    Get student by ID
    """
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    """
    get student by name
    """
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}
