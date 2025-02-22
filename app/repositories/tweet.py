from sqlalchemy.orm import Session
from app.models.tweet import Tweet
from app.schemas.tweet import TweetSchema

def create_tweet(db: Session, tweet: TweetSchema):
    db_tweet = Tweet(
        contenido=tweet.contenido,
        autor_id=tweet.autor_id
    )
    db.add(db_tweet)
    db.commit()
    db.refresh(db_tweet)
    return db_tweet

def get_tweets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tweet).offset(skip).limit(limit).all()