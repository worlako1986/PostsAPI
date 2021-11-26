import datetime
from enum import unique
from operator import index
from peewee import *
import datetime
from database import BaseModel as BM
from abc import ABC, abstractmethod


class Jsonify(ABC):

    @abstractmethod
    def __json__():
        pass


class User(BM):
    user_id = AutoField()
    email = CharField(max_length=255, unique = True)
    full_name = CharField(max_length=100, null = False, index = True)
    password  = CharField(max_length=255, null = False)
    is_active = BooleanField(default = True)
    age   = IntegerField(default = 0)
    join_date = DateTimeField(null = False, default = datetime.datetime.now())

    class Meta:
        table_name = "users"
    
    def __json__(self):
        return {

            "user_id": self.user_id,
            "email": self.email,
            "full_name": self.full_name,
            "is_active": self.is_active,
            "age": self.age,
        }

    def __jwt_payload__(self):
        return {
            "user_id": self.user_id,
            "is_active": self.is_active,
            "full_name": self.full_name,
        }

class Posts(BM):
    post_id = AutoField()
    title = CharField(max_length=100)
    content = TextField()
    published = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref='posts')

    class Meta:
        table_name = "posts"

    
    def __json__(self):
        return {
            "post_id": self.post_id,
            "title": self.title,
            "content": self.content,
            "published": self.published
        }




