from jose import (JOSEError, jwt)
from datetime import timedelta, datetime
import json


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(payload: dict):
    to_encode = payload.copy()
    # build expire time
    expire_time = datetime.now() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})
    # build jwt token
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt
