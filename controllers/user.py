from datetime import timedelta
from sqlalchemy.orm import Session
from services import user
from utils.jwt import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, verify_token

def create(username: str, password: str, db: Session):
    created_user = user.create(username, password, db)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": username}, expires_delta=access_token_expires)
    return {"user": created_user, "access_token": access_token, "token_type": "bearer"} 

def get_by_id(db: Session, user_id: int):
    return user.get_by_id(db, user_id)

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return user.get_users(db, skip=skip, limit=limit)

def update(username: str, password: str, user_id: int, db: Session):
    return user.update(db, user_id, password, username)

def delete(db: Session, user_id: int):
    return user.delete(db, user_id)

def authenticate(username: str, password: str, db: Session):
    db_user = user.login(username, password, db)
    if db_user:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": db_user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    return None
