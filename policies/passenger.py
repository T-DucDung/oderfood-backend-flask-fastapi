from starlette.middleware.base import BaseHTTPMiddleware
class NotAuth(BaseHTTPMiddleware):
 async def dispatch(self, request, call_next):
    print("ok")
    response = await call_next(request)

    return response

# from starlette.authentication import SimpleUser  # or a custom user model
# from starlette_auth_toolkit.base.backends import BaseTokenAuth

# class TokenAuth(BaseTokenAuth):
#     async def verify(self, token: str):
#         # In practice, request the database to find the token object
#         # associated to `token`, and return its associated user.
#         if token != "abcd":
#             return None
#         return SimpleUser("bob")
