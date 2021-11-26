import datetime
from fastapi import (HTTPException, status)
from model import (User)
import schemamodel as sml
from database import (FastAPIDB)
from hashpw import (hash_password)
from oauth2 import (create_access_token)



def retrive_users():
    conn, cursor, error, errorcode = FastAPIDB.connection()
    try:
        queryUser = "SELECT users.user_id, users.full_name, users.is_active, users.join_date, users.age, users.email FROM users"
        cursor.execute(queryUser)
        result = cursor.fetchall()
        return result
    except error as err:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(err))

def log_user_to_db(user: sml.User):

    try:

        new_user = User()
        new_user.full_name = user.full_name
        new_user.password = hash_password(user.password)
        new_user.email = user.email
        new_user.age = user.age
        new_user.is_active = True
        new_user.join_date = datetime.datetime.now()

        new_user.save()
        return new_user

    except Exception as e:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))


def update_user_details(user_id:int, user_: sml.UpdateUser):
    try:
        user = User.get_or_none(User.user_id == user_id)
        if user:
            user.full_name = user_.full_name
            user.age = user_.age
            user.save()
        else:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"User with id: {user_id} not found")
        
        return user.__json__()

    except Exception as e:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(e))


def retrive_user(user_id: int):
    conn, cursor, error, errorcode = FastAPIDB.connection()
    try:
        queryUser = "SELECT users.user_id, users.full_name, users.is_active, users.join_date, users.age, users.email FROM users WHERE users.user_id = %(user_id)s "
        cursor.execute(queryUser, {
            "user_id": user_id
        })
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result:
            return result
        else:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"User with id: {user_id} not found")

    except error as err:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(err))


def remove_user(user_id: int):
    try:
        user = User.get_or_none(User.user_id == user_id)
        if user:
            user.delete_instance()
            return user.__json__()
        else:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"User with id: {user_id} not found")
    
    except Exception as e:
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))


def authenticate(data: sml.Login):
    try:
        user =  User.get_or_none(User.email == data.username)
        if user:
            if hash_password(data.password) == user.password:
                access_token = create_access_token(user.__jwt_payload__())
                return {"access_token": access_token, "token_type": "bearer"}
            else:
                print("worrrr")
                raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Invalid password and email")
        else:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Invalid password and email")

    except Exception as e:
        print("detail: ",str(e))
        raise HTTPException(status_code= status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))