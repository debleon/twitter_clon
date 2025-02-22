from sqlalchemy.orm import Session
from app.repositories.tweet import create_tweet, get_tweets
from app.schemas.tweet import TweetSchema

def post_tweet(db: Session, tweet_data: TweetSchema):
    return create_tweet(db, tweet_data)

def fetch_tweets(db: Session, skip: int = 0, limit: int = 10):
    return get_tweets(db, skip, limit)