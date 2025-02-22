# repositories/user.py (Repositorio de Usuario en repositories/)
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserSchema

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserSchema):
    db_user = User(
        nombre=user.nombre,
        username=user.username,
        email=user.email,
        contraseña=user.contraseña,
        foto_perfil=user.foto_perfil
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user