from flask import jsonify, abort, make_response
import jwt


def verify(token):
    verifying_key = "afkawfl1421ADwawd!%@qdawdajlkwdjaldjzlcjwidj"
    
    decoded = jwt.decode(token, verifying_key, algorithms='HS256')
    return decoded