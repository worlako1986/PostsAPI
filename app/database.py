from peewee import *
import mysql.connector
from mysql.connector import errorcode




def orm_connection():
    conn = MySQLDatabase(
        database = 'fastapi',
        user='root',
        #password='db_password',
        host='127.0.0.1',
        port=3306
        )
    return conn

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = orm_connection()


class FastAPIDB:
    """mysql connection to fastapi database"""
    @classmethod
    def connection(cls):
        """Return a tuple of the connection to the database and the cursor"""
        conn = mysql.connector.connect(
        database='fastapi',
        user='root',
        #password='db_password',
        host='127.0.0.1',
        port=3306
        )

        return (conn, conn.cursor(dictionary = True), mysql.connector.Error, errorcode)

        
    