from fastapi import FastAPI
from controllers import users_controller , register_controller

app= FastAPI()

app.include_router(users_controller.router)
app.include_router(register_controller.router)
