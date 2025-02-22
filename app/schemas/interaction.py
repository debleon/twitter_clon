from pydantic import BaseModel
import datetime
class InteractionSchema(BaseModel):
    id: int
    tipo_interaccion: str
    fecha_interaccion: datetime.datetime
    usuario_id: int
    tweet_id: int

    class Config:
        orm_mode = True