from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    bio=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to="profile_picture")

class Education(models.Model):
    school=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    fos=models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.DateTimeField()
    desc=models.TextField()
    
class Experience(models.Model):
    job=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    start=models.DateTimeField()
    end=models.DateTimeField()
    description=models.TextField()
    
class CreateProfile(models.Model):
    company=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    location=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    github=models.CharField(max_length=100)
    bio=models.CharField(max_length=100)
    twiter=models.URLField(max_length=100)
    facebook=models.URLField(max_length=100)
    youtube=models.URLField(max_length=100)
    linkdin=models.URLField(max_length=100)
    insta=models.URLField(max_length=100)
    
class Login(models.Model):
    emailadd=models.EmailField()
    password=models.CharField(max_length=100)
    
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm=models.CharField(max_length=100)
    