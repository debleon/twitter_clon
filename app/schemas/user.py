from pydantic import BaseModel
import datetime

class UserSchema(BaseModel):
    id: int
    nombre: str
    username: str
    email: str
    foto_perfil: str | None
    fecha_registro: datetime.datetime

    class Config:
        orm_mode = True
