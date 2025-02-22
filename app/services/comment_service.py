from sqlalchemy.orm import Session
from app.repositories.comment import create_comment, get_comments_by_tweet
from app.schemas.comment import CommentSchema

def add_comment(db: Session, comment_data: CommentSchema):
    return create_comment(db, comment_data)

def fetch_comments_by_tweet(db: Session, tweet_id: int):
    return get_comments_by_tweet(db, tweet_id)
