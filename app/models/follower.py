# follower.py (Modelo de Seguidores)
# user.py (Modelo de Usuario)
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class Follower(Base):
    __tablename__ = "seguidores"

    id = Column(Integer, primary_key=True, index=True)
    seguidor_id = Column(Integer, ForeignKey("usuarios.id"))
    seguido_id = Column(Integer, ForeignKey("usuarios.id"))
    fecha_seguimiento = Column(DateTime, default=datetime.datetime.utcnow)

    seguidor = relationship("User", foreign_keys=[seguidor_id])
    seguido = relationship("User", foreign_keys=[seguido_id])
