from fastapi import APIRouter
from services.userservices import user_services

router = APIRouter()

@router.get("/{user_id}", tags=["users"])
async def read_users(user_id: int):
    print("haha")
    print(user_id)
    return user_services.get_user(user_id)