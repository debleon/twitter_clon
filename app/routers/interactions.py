# routers/interaction.py (Rutas de Interacciones en routers/)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.interaction import InteractionSchema
from app.services.interaction_service import add_interaction, fetch_interactions_by_tweet

router = APIRouter()

@router.post("/", response_model=InteractionSchema)
def create_interaction(interaction: InteractionSchema, db: Session = Depends(get_db)):
    return add_interaction(db, interaction)

@router.get("/by_tweet/{tweet_id}", response_model=list[InteractionSchema])
def get_interactions(tweet_id: int, db: Session = Depends(get_db)):
    return fetch_interactions_by_tweet(db, tweet_id)