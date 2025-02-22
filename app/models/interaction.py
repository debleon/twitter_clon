from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

# interaction.py (Modelo de Interacciones)
class Interaction(Base):
    __tablename__ = "interacciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo_interaccion = Column(String(50), nullable=False)  # Like, Retweet, etc.
    fecha_interaccion = Column(DateTime, default=datetime.datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tweet_id = Column(Integer, ForeignKey("tweets.id"))

    usuario = relationship("User", back_populates="interacciones")
    tweet = relationship("Tweet", back_populates="interacciones")