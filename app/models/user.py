#user.py (Modelo de Usuario)
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    foto_perfil = Column(String, nullable=True)
    fecha_registro = Column(DateTime, default=datetime.datetime.utcnow)

    tweets = relationship("Tweet", back_populates="autor")
    comentarios = relationship("Comment", back_populates="autor")
    interacciones = relationship("Interaction", back_populates="usuario")
    seguidores = relationship("Follower", back_populates="seguido")