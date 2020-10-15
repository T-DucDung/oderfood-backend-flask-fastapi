 
import jwt 
import time
import simplejson as json
from datetime import datetime, timedelta, timezone
def sign(payload=None):
    dt = datetime.now() + timedelta(seconds=60)   
    payload = {
        "userId":1,
        "name":"admin",
        "phone":"0356798938",
        "iat": datetime.now(),
        "exp": dt
        }
    signing_key = "afkawfl1421ADwawd!%@qdawdajlkwdjaldjzlcjwidj"
    encoded = jwt.encode(payload, signing_key, algorithm='HS256')
    return encoded