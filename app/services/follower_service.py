from sqlalchemy.orm import Session
from app.repositories.follower import follow_user, get_followers
from app.schemas.follower import FollowerSchema

def follow_user_service(db: Session, follower_data: FollowerSchema):
    return follow_user(db, follower_data)

def fetch_followers(db: Session, user_id: int):
    return get_followers(db, user_id)