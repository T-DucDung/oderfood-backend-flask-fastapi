
from sqlalchemy.orm import Session
from models import users_model , users_schema


def get_user(db: Session, user_id: int):
    return db.query(users_model.User).filter(users_model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(users_model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: users_schema.UserCreate):
    db_user = users_model.User(content=user.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user