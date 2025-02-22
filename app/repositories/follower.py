from sqlalchemy.orm import Session
from app.models.follower import Follower
from app.schemas.follower import FollowerSchema

def follow_user(db: Session, follower: FollowerSchema):
    db_follower = Follower(
        seguidor_id=follower.seguidor_id,
        seguido_id=follower.seguido_id
    )
    db.add(db_follower)
    db.commit()
    db.refresh(db_follower)
    return db_follower

def get_followers(db: Session, user_id: int):
    return db.query(Follower).filter(Follower.seguido_id == user_id).all()