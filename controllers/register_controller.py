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


@router.get("/registers/", response_model=List[register_schema.Register])
@customer
async def read_registers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    registers = register_service.get_registers(db, skip=skip, limit=limit)
    return registers


@router.get("/registers/{register_id}", response_model= register_schema.Register)
async def read_register(register_id: int, db: Session = Depends(get_db)):
    db_register = register_service.get_register(db, register_id=register_id)
    print(db_register)
    if db_register is None:
        raise HTTPException(status_code=404, detail="Register not found")
    return db_register
    # return {'id':1 , 'content':'hihi'}


