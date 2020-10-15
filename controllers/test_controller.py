from typing import List
from fastapi import APIRouter ,Depends, HTTPException
from services.registerservice import register_service
from models.register import register_model,register_schema
from sqlalchemy.orm import Session
from config.model_global import SessionLocal ,engine
from policies.customer import customer
router = APIRouter()

# users_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/test")
@customer
def create_user():
    return "Hello"

