from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Jhon",
        "age": 17,
        "year": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str


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

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    """
    get student by name
    """
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    """
    create student
    """
    if student_id in students:
        return {"error": "student exists"}
    
    students[student_id] = student
    return students[student_id]
