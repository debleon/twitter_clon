# main.py (Archivo Principal)
import sys
import os
from fastapi import FastAPI

# Agregar la ruta del directorio base al sys.path para evitar problemas de importación
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.routers import auth, users, tweets, interactions
from app.core.database import engine, Base
from app.core.config import settings

# Crear tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Twitter Clone API", version=settings.PROJECT_VERSION, description="API REST para un clon de Twitter con FastAPI y PostgreSQL")

# Registrar routers (endpoints)
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tweets.router, prefix="/tweets", tags=["Tweets"])
app.include_router(interactions.router, prefix="/interactions", tags=["Interactions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Twitter Clone API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
