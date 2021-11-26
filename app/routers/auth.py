from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Response,
    Request
)

from fastapi.params import Depends
import schemamodel as sml
from database import (FastAPIDB)
from model import (User)
import userfunc as uft
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    data = uft.authenticate(data)
    if data:
        return data
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= {"message": "Invalid user email or password", "is_error": True}) 


