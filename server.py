# Library
import uvicorn
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from pathlib import PurePosixPath
# Auth
from helpers.jwt_tool import sign, verify
from policies.customer import CustomerMiddleware
from policies.passenger import NotAuth
from starlette.responses import JSONResponse,Response, RedirectResponse
# Controller
from controllers import register_controller
from controllers import users_controller
from controllers import test_controller
from controllers import login_controller
# App
# from app.app1 import app1
# from app.app2 import app2
# Body
app = FastAPI()

# Add policies
#app.add_middleware(CustomerMiddleware)
# app.mount("/api",app1)
white_list = ["docs", "openapi.json"]


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    print(request.url.path)
    if(request.url.path == "/"):
        print("home")
    else:
        if PurePosixPath(request.url.path).parts[1] in white_list:
            print("no need to auth")
        else:
            print("must auth")
            try:
                print(sign())
                print(request.url.path)
                print(white_list_routes)
                if request.url.path in white_list_routes:
                    # print(request.url.path)
                    # print(white_list_routes)
                    response = await call_next(request)
                    return response

                auth = request.headers['Authorization']

                token = auth.split(" ")
                if(token[0] != "Bearer"):
                    return JSONResponse(
                        {'detail': 'Not auth'}
                    )
                    #  return Response({'detail':'Not auth'},status_code=401)
                # print("OK")
                data = verify(token[1])

                request.state.user = data

                response = await call_next(request)
                return response
            except:
                return JSONResponse(
                    {'detail': 'Not auth'}
                )

    response = await call_next(request)
    return response
# app2.add_middleware(NotAuth)
# app.mount("/api/v2",app2)


# Router
# app2.include_router(login_controller.router)
    # app2.include_router(users_controller.router)
    # app2.include_router(register_controller.router)
    # app2.include_router(test_controller.router)
app.include_router(users_controller.router)
# app1.include_router(register_controller.router)
# app1.include_router(test_controller.router)
