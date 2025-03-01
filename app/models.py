from django.contrib.auth.models import User
from django.db import models
class CustomUserModel(User):
    gender=models.CharField(max_length=10,choices=[['male','Male'],['female','Female']])
    profile_picture=models.ImageField(upload_to='profile_picture/')
    