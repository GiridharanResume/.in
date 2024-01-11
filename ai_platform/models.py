from django.db import models
import uuid
from datetime import datetime



# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class KTcourse(models.Model):
     user_id = models.UUIDField( default = uuid.uuid4,auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
     firstname = models.CharField(max_length=100)
     lastname=models.CharField(max_length=100,default="")
     email=models.CharField(max_length=200)
     college=models.CharField(max_length=100)
     Register_date = models.DateField(auto_now=True)
     close_date = models.DateField(auto_now=True)


class course_name(models.Model):
    user_id = models.UUIDField( default = uuid.uuid4,auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    name=models.CharField(max_length=100,null=True)    
    description = models.CharField(max_length=250,null=True)



class signup(models.Model):
    user_id = models.UUIDField( default = uuid.uuid4,auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    name = models.CharField(max_length=100 , null=True) 
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100)
    CollegeName = models.CharField(max_length=100)
    Degree = models.CharField(max_length=100)
    Date = models.DateField(auto_now=True)
    Gender = models.TextField()
    Phoneno = models.CharField(max_length=10)
    State =models.CharField(max_length=100,default="")
    DOB = models.CharField(max_length=15 ,null=True)

class mentor(models.Model):
     id = models.UUIDField( default = uuid.uuid4,auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
     image = models.ImageField(upload_to='images/')
     name = models.CharField(max_length=100 , null=True)
     position =models.CharField(max_length=100, null=True)

class Admin (models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)   
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class subadmin (models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)   
    date_created = models.DateTimeField(auto_now_add=True, null=True)


     
    
class Staff_admin (models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)   
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Student_subadmin (models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=100, null=True)   
    date_created = models.DateTimeField(auto_now_add=True, null=True)    