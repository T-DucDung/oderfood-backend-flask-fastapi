from typing import List
from fastapi import APIRouter ,Depends, HTTPException
from services.userservices import user_services
from models import users_model , users_schema
from sqlalchemy.orm import Session
from models.model_global import SessionLocal ,engine

router = APIRouter()

# users_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/users/", response_model=List[users_schema.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_services.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=users_schema.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_services.get_user(db, user_id=user_id)
    print(db_user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/", response_model=users_schema.User)
def create_user(user: users_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_services.get_user(db, user_id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail="Id already existed")
    return user_services.create_user(db=db, user=user)
