from database import (
    BaseModel,
    orm_connection
)
import peewee


def create_tables():
    try:
        conn = orm_connection()
        models = [

            # Load all class or model inherit from BaseModel
            obj  for obj in BaseModel.__subclasses__()
            
            ]
            
        print(f"Models: {models}")

        # Create tables
        conn.create_tables(models)
        conn.close()
        #peewee.create_model_tables(models)

    except Exception as e:
        print(f"Error: {str(e)}")
