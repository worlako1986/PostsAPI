from fastapi import (FastAPI, Response, Request, status, HTTPException)
from  routers import(
    post,
    user,
    auth
)
import create_table_in_database as dbt


# Create instance of fast-api
app = FastAPI()

@app.get('/')
def root():
    return {'message': 'login'}


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


#dbt.create_tables()



