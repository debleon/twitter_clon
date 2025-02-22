from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionSchema

def create_interaction(db: Session, interaction: InteractionSchema):
    db_interaction = Interaction(
        tipo_interaccion=interaction.tipo_interaccion,
        usuario_id=interaction.usuario_id,
        tweet_id=interaction.tweet_id
    )
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

def get_interactions_by_tweet(db: Session, tweet_id: int):
    return db.query(Interaction).filter(Interaction.tweet_id == tweet_id).all()