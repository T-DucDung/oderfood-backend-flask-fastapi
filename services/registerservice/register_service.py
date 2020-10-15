
from sqlalchemy.orm import Session
from models.register import register_model , register_schema


def get_register(db: Session, register_id: int):
    return db.query(register_model.Register).filter(register_model.Register.id == register_id).first()

def get_registers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(register_model.Register).offset(skip).limit(limit).all()
