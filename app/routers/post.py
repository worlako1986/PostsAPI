from fastapi import (FastAPI, Response, Request, status, HTTPException, APIRouter)
from fastapi.params import Body
from random import randrange
from schemamodel import (
    Post,
    UpdatePost
    
    )
import postsfunc as ptf
router = APIRouter(tags= ["Posts"])
#router = APIRouter(prefix = "/posts", tags= ["Posts"])




@router.get("/posts/{id}")
def getPost(id: int):
    post = ptf.getPostById(id)
    if post:
        return post
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} not found")



@router.get('/posts')
def getPost():
    result = ptf.getAllPost()
    return result


@router.post('/posts', status_code = status.HTTP_201_CREATED)
def createPost(post: Post):
    newPost = ptf.createPost(post)
    return newPost

@router.delete("/posts/{id}", status_code = status.HTTP_204_NO_CONTENT)
def deletePost(id: int):
    result = ptf.deletePosts(id)
    if result:
        return {"message": f"Post with id: {id} successfully deleted.", "data":result}
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} not found.")


@router.put("/posts/{id}")
def updatePost(id: int, post: UpdatePost):
    result = ptf.updatePost(id, post)
    if result:
        return result
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} not found")
