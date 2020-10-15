
import bcrypt

def checkHash(password,hashed):
    if bcrypt.checkpw(password, hashed):
        return true
    else:
        return false