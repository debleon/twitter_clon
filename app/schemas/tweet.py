from pydantic import BaseModel
import datetime

class TweetSchema(BaseModel):
    id: int
    contenido: str
    fecha_creacion: datetime.datetime
    num_likes: int
    autor_id: int

    class Config:
        orm_mode = True