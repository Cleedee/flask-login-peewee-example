from peewee import *

db = SqliteDatabase('users.db')

class User(Model):
    email = CharField()
    name = CharField()
    password = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.
