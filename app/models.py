from django.db import models

# Create your models here.
from mongoengine import *
connect('mydb')
class Books1(Document):
    title = StringField(required=True)
    language = StringField(max_length=50)
    author = StringField(max_length=50)
