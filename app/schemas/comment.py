from pydantic import BaseModel
import datetime
class CommentSchema(BaseModel):
    id: int
    contenido: str
    num_likes: int
    fecha_comentario: datetime.datetime
    autor_id: int
    tweet_id: int

    class Config:
        orm_mode = True