from sqlalchemy.orm import Session
from models.user import Usuario

def create(username: str, password: str, db: Session):
    hashed_password = "hash_password_logic_here"  # Implemente a lógica de hash de senha adequada aqui
    new_user = Usuario(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username, "password": new_user.hashed_password}

def get_by_id(db: Session, user_id: int):
    return db.query(Usuario).filter(Usuario.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Usuario).offset(skip).limit(limit).all()

def update(db: Session, user_id: int, password: str, username: str):
    db_user = db.query(Usuario).filter(Usuario.id == user_id).first()
    db_user.hashed_password = "hash_updated_password_logic_here"  # Implemente a lógica de atualização da senha adequada aqui
    db_user.username = username
    db.commit()
    db.refresh(db_user)
    return db_user

def delete(db: Session, user_id: int):
    db_user = db.query(Usuario).filter(Usuario.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}

def login(username: str, password: str, db: Session):
    return db.query(Usuario).filter(
        Usuario.username == username,
        Usuario.hashed_password == "hash_password_logic_here"
    ).first()