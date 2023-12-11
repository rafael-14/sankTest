from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers import user
from pydantic import BaseModel
from typing import Union

class UserRequest(BaseModel):
    username: Union[str, None] = None
    password: Union[str, None] = None
    user_id: Union[int, None] = None

router = APIRouter()

@router.post("/api/users", response_model=dict)
def create(body: UserRequest, db: Session = Depends(get_db)):
    return user.create(body.username, body.password, db)

@router.post("/api/login", response_model=dict)
def login(body: UserRequest, db: Session = Depends(get_db)):
    return user.authenticate(body.username, body.password, db)

@router.get("/api/user/{user_id}")
def find_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.get_by_id(db, user_id)

@router.get("/api/users")
def find_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user.get_users(db, skip=skip, limit=limit)

@router.put("/api/user/{user_id}")
def update(body: UserRequest, user_id: int, db: Session = Depends(get_db)):
    return user.update(body.username, body.password, user_id, db)

@router.delete("/api/user/{user_id}")
def delete_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.delete(db, user_id)
