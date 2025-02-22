# tweet.py (Modelo de Tweets)
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class Tweet(Base):
    __tablename__ = "tweets"

    id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.datetime.utcnow)
    num_likes = Column(Integer, default=0)
    autor_id = Column(Integer, ForeignKey("usuarios.id"))

    autor = relationship("User", back_populates="tweets")
    comentarios = relationship("Comment", back_populates="tweet")
    interacciones = relationship("Interaction", back_populates="tweet")
