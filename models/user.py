from sqlalchemy import Column, Integer, String

from database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
