from sqlalchemy.orm import Session
from app.repositories.user import get_user_by_username, create_user
from app.schemas.user import UserSchema

def register_user(db: Session, user_data: UserSchema):
    existing_user = get_user_by_username(db, user_data.username)
    if existing_user:
        raise ValueError("El usuario ya existe")
    return create_user(db, user_data)