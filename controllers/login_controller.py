from typing import List
from typing import Optional
from fastapi import APIRouter ,Depends, HTTPException, Header, Request
from services.registerservice import register_service
from models.register import register_model,register_schema
from sqlalchemy.orm import Session
from config.model_global import SessionLocal ,engine
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from helpers.jwt_tool import sign
router = APIRouter()

# users_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/api/v2/login")
async def create_user(request: Request):
    
    return  sign()