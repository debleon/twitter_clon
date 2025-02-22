from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentSchema

def create_comment(db: Session, comment: CommentSchema):
    db_comment = Comment(
        contenido=comment.contenido,
        autor_id=comment.autor_id,
        tweet_id=comment.tweet_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_tweet(db: Session, tweet_id: int):
    return db.query(Comment).filter(Comment.tweet_id == tweet_id).all()