from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("e22ffc52-83f3-4126-bc33-d1c432b9beb0"), 
        first_name="Jamila", 
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("50698eaa-a11d-4796-871d-be0108738102"), 
        first_name="Alex", 
        last_name="Jonse",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api/v1/users/")
async def fetch_users():
    return db
