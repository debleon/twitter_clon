# comment.py (Modelo de Comentarios)
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class Comment(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    num_likes = Column(Integer, default=0)
    fecha_comentario = Column(DateTime, default=datetime.datetime.utcnow)
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    tweet_id = Column(Integer, ForeignKey("tweets.id"))

    autor = relationship("User", back_populates="comentarios")
    tweet = relationship("Tweet", back_populates="comentarios")