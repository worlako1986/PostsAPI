from fastapi import (FastAPI, Response, Request, status, HTTPException, APIRouter)
from fastapi.params import Body
from random import randrange
import userfunc as uft

from schemamodel import (
    User,
    UpdateUser
    
    )

router = APIRouter(tags=["Users"])


@router.get("/users", status_code= status.HTTP_200_OK)
def get_users():
    result = uft.retrive_users()
    print("result: ",result)
    if result:
        return result
    HTTPException(status_code= status.HTTP_200_OK, detail= "Non data found")


@router.post("/users", status_code= status.HTTP_201_CREATED)
def create_user(user: User):
    result = uft.log_user_to_db(user)
    if result:
        return result
    raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Error occur whilst creating user")


@router.put("/users/{user_id}", status_code= status.HTTP_201_CREATED)
def update_user(user_id:int, user: UpdateUser):
    data = uft.update_user_details(user_id, user)
    if data:
        return data
    else:
        HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= "error occur whilst updating user")

@router.get("/users/{user_id}")
def get_user(user_id: int):
    data = uft.retrive_user(user_id)
    if data:
        return data
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"User with id: {user_id} not found")


@router.delete("/users/{user_id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    result = uft.remove_user(user_id)
    if result:
        return result
    else:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"User with id: {user_id} not found")