# routers/follower.py (Rutas de Seguidores en routers/)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.follower import FollowerSchema
from app.services.follower_service import follow_user_service, fetch_followers

router = APIRouter()

@router.post("/", response_model=FollowerSchema)
def follow_user(follower: FollowerSchema, db: Session = Depends(get_db)):
    return follow_user_service(db, follower)

@router.get("/followers/{user_id}", response_model=list[FollowerSchema])
def get_followers(user_id: int, db: Session = Depends(get_db)):
    return fetch_followers(db, user_id)