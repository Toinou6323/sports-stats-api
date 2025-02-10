from fastapi import FastAPI
from database import engine, Base
from auth import router as auth_router
from models import router as models_router

# Initialisation de l'application FastAPI
app = FastAPI()

# Création des tables dans la base de données
Base.metadata.create_all(bind=engine)

# Inclusion des routes d'authentification et des modèles
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(models_router, prefix="/api", tags=["models"])

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API Sports Stats !"}
