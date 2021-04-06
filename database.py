from peewee import *
from flask_login import UserMixin

db = SqliteDatabase('users.db')

class User(Model, UserMixin):
    email = CharField()
    name = CharField()
    password = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.
