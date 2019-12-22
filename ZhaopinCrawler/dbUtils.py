from peewee import *
import datetime

db = MySQLDatabase("mytest", host="47.112.28.50", port=3306, user="root", passwd="root")
db.connect()

class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)

if __name__ == '__main__':
    User.create()