# routers/comment.py (Rutas de Comentarios en routers/)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.comment import CommentSchema
from app.services.comment_service import add_comment, fetch_comments_by_tweet

router = APIRouter()

@router.post("/", response_model=CommentSchema)
def create_comment(comment: CommentSchema, db: Session = Depends(get_db)):
    return add_comment(db, comment)

@router.get("/by_tweet/{tweet_id}", response_model=list[CommentSchema])
def get_comments(tweet_id: int, db: Session = Depends(get_db)):
    return fetch_comments_by_tweet(db, tweet_id)