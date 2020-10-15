from fastapi import FastAPI
from controllers import  register_controller
from controllers import  users_controller
from controllers import  test_controller


app= FastAPI()
app.include_router(users_controller.router)
app.include_router(register_controller.router)
app.include_router(test_controller.router)