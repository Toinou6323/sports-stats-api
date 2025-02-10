from fastapi import APIRouter, Depends
from authlib.integrations.starlette_client import OAuth
from starlette.requests import Request
from database import SessionLocal
from models import User

router = APIRouter()

oauth = OAuth()
# Ajouter la configuration OAuth ici (Google, Facebook, Apple)

@router.get("/login/google")
async def login_google(request: Request):
    return await oauth.google.authorize_redirect(request, "http://localhost:8000/auth/google")
