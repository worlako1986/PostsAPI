from operator import pos
from fastapi import (HTTPException, status)
from mysql.connector import cursor, errorcode
from model import (Posts)
import schemamodel as sml
from database import (FastAPIDB)


def createPost_(post: sml.Post):
    conn, cursor, error, errorcode = FastAPIDB.connection()
    insertPosts = "INSERT INTO posts (title, content) VALUES(%s, %s)"
    data = (post.title, post.content)
    cursor.execute(insertPosts, data)
    conn.commit()

    # Get inserted post
    postId = cursor.lastrowid
    queryPost = "SELECT * FROM posts WHERE id = %(id)s"
    cursor.execute(queryPost, {"id":postId})
    newPost = cursor.fetchone()


    cursor.close()
    conn.close()

    return newPost


def createPost(post: sml.Post):
    newPost = Posts()
    newPost.title = post.title
    newPost.content = post.content
    newPost.save()
    return newPost



def getAllPost():
    conn, cursor, error, errorcode = FastAPIDB.connection()

    result = []
    query = f"SELECT * FROM posts;"

    cursor.execute(query)
    result  = cursor.fetchall()
    #for title, content in cursor:
    #    result.append({"title":title, "content":content})


    cursor.close()
    conn.close()
    return result

def getPostById(id: int):
    conn, cursor, error, errorcode = FastAPIDB.connection()
    try:
        queryPost = "SELECT * FROM posts WHERE id = %(id)s"
        cursor.execute(queryPost, {"id": id})
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
    except error as err:
        print(err)
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(err))
    finally:
        cursor.close()
        conn.close()


def updatePost(id: int, post: sml.UpdatePost):

    conn, cursor, error, errorcode = FastAPIDB.connection()
    try:

        updatePost_ = "UPDATE posts SET title = %(title)s, content = %(content)s WHERE id = %(id)s"
        cursor.execute(updatePost_, {
            "title": post.title,
            "content": post.content,
            "id":id
        })
        conn.commit()

        # Get updated post
        queryPost = "SELECT * FROM posts WHERE id = %(id)s"
        cursor.execute(queryPost, {"id": id})
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
    except error as err:
        HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(err))
    finally:
        cursor.close()
        conn.close()

def deletePosts(id: int):
    conn, cursor, error, errorcode = FastAPIDB.connection()
    try:
        queryPost  = "SELECT * FROM posts WHERE id = %(id)s"
        cursor.execute(queryPost, {"id": id})
        result = cursor.fetchone()
        if result:
            deletePost = "DELETE FROM posts WHERE id = %(id)s"
            cursor.execute(deletePost, {"id": id})
            conn.commit()

        cursor.close()
        conn.close()
        return result
    except error as err:
        HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = str(err) )
    finally:
        cursor.close()
        conn.close()