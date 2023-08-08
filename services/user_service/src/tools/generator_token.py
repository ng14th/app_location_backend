import jwt
from datetime import datetime, timedelta
from typing import Union, Any
from settings import settings
from core.exceptions.reponse_exception import ErrorResponeException
from core.exceptions.mapping_exception import get_error_code
import bcrypt

def generate_jwt_token(data_user : Union[dict, Any]):
    expire = datetime.utcnow() + timedelta(seconds=60*60) # 1 hour
    to_encode = {"exp": expire, "data_user": data_user}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.SECURITY_ALGORITHM)
    return encoded_jwt

def generate_jwt_refresh_token(data_user : Union[dict, Any]):
    expire = datetime.utcnow() + timedelta(seconds=3600*24) # 1 day
    to_encode = {"exp": expire, "data_user": data_user}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.SECURITY_ALGORITHM)
    return encoded_jwt

def decode_jwt_token(token):
    try :
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
        if payload.get('exp') < int(datetime.now().timestamp()):
            raise ErrorResponeException(**get_error_code(99403))
        return payload.get('data_user')
    except:
        raise ErrorResponeException(**get_error_code(99403))

def hass_password(password):
    password = bytes(password, 'utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password,salt)
    return hashed

def check_password(password, password_hash):
    password = bytes(password, 'utf-8')
    if bcrypt.checkpw(password,password_hash):
        return True
    else:
        return False
    
def refresh_token(refresh_token: str):
    try:
        refresh_token_payload = decode_jwt_token(refresh_token)
        username = refresh_token_payload["data_user"]
        access_token = generate_jwt_token(username)
        refresh_token_generate = generate_jwt_refresh_token(username)
        return {"access_token": access_token, "refresh_token_generate": refresh_token_generate,"username": username}
    except :
        raise ErrorResponeException(**get_error_code(10401))