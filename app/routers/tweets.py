# routers/tweet.py (Rutas de Tweets en routers/)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.tweet import TweetSchema
from app.services.tweet_service import post_tweet, fetch_tweets

router = APIRouter()

@router.post("/", response_model=TweetSchema)
def create_tweet(tweet: TweetSchema, db: Session = Depends(get_db)):
    return post_tweet(db, tweet)

@router.get("/", response_model=list[TweetSchema])
def get_all_tweets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return fetch_tweets(db, skip, limit)