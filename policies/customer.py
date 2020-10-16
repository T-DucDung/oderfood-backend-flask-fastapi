from starlette.middleware.base import BaseHTTPMiddleware
from helpers.jwt_tool import sign, verify
from starlette.responses import JSONResponse,Response
from starlette.requests import Request
from flask import g
class CustomerMiddleware(BaseHTTPMiddleware):
 async def dispatch(self, request, call_next):
    
    try:
        
        # print(sign())
        auth = request.headers['Authorization']
        token = auth.split(" ")
        # print(token)
        if(token[0]!="Bearer"):
            return JSONResponse(
                {'detail':'Not auth'}
             )
            #  return Response({'detail':'Not auth'},status_code=401)
        # print("OK")
        data = verify(token[1])
        request.state.user = data

        response = await call_next(request)
        return response
    except:
        return JSONResponse(
                {'detail':'Not auth'}
        )
    



