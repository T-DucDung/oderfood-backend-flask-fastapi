#Library
import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException
#Auth
from policies.customer import CustomerMiddleware
from policies.passenger import NotAuth
#Controller
from controllers import  register_controller
from controllers import  users_controller
from controllers import  test_controller
from controllers import login_controller
#App
# from app.app1 import app1
# from app.app2 import app2
#Body
app = FastAPI()

# Add policies
app.add_middleware(CustomerMiddleware)
# app.mount("/api",app1)

# app2.add_middleware(NotAuth)
# app.mount("/api/v2",app2)


#Router
# app2.include_router(login_controller.router)
    # app2.include_router(users_controller.router)
    # app2.include_router(register_controller.router)
    # app2.include_router(test_controller.router)
app.include_router(users_controller.router)
# app1.include_router(register_controller.router)
# app1.include_router(test_controller.router)