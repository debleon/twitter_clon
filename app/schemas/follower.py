from pydantic import BaseModel
import datetime
class FollowerSchema(BaseModel):
    id: int
    seguidor_id: int
    seguido_id: int
    fecha_seguimiento: datetime.datetime

    class Config:
        orm_mode = True