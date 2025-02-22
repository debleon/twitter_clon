from sqlalchemy.orm import Session
from app.repositories.interaction import create_interaction, get_interactions_by_tweet
from app.schemas.interaction import InteractionSchema

def add_interaction(db: Session, interaction_data: InteractionSchema):
    return create_interaction(db, interaction_data)

def fetch_interactions_by_tweet(db: Session, tweet_id: int):
    return get_interactions_by_tweet(db, tweet_id)