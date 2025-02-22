# routers/user.py (Rutas de Usuario en routers/)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserSchema
from app.services.user_service import register_user

router = APIRouter()

@router.post("/register", response_model=UserSchema)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return register_user(db, user)