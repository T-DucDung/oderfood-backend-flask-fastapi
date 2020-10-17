from starlette.middleware.base import BaseHTTPMiddleware
from helpers.jwt_tool import sign, verify
from starlette.responses import JSONResponse,Response, RedirectResponse
from starlette.requests import Request
from config.routes import white_list_routes

class CustomerMiddleware(BaseHTTPMiddleware):
 async def dispatch(self, request, call_next):
    
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
    

