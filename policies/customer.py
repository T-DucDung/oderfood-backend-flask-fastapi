
from flask import request, Response , jsonify, g
from helpers.jwt_tool import  verify
from helpers.jwt_tool import sign
from functools import wraps
def customer(f):
   @wraps(f)
   def decorator(*args, **kwargs):
        
        try:
            print("ok")
            auth = request.headers['Authorization']
            token = auth.split(" ")
            # print(token[0])
            if(token[0] != "Bearer"):
                return jsonify({'message': 'a valid token is missing', "code":403})
            data = verify(token[1])
            g.data = data
        except:
            return jsonify({'message': 'a valid token is missing', "code":403})

        return f(*args, **kwargs)
   return decorator