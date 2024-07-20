from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     usertype=models.CharField(max_length=100)

class Department(models.Model):
     Dep_Name=models.CharField(max_length=100)

class Student(models.Model):
    dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=200)
    Phone=models.BigIntegerField()


class Teacher(models.Model):
    dep_id=models.ForeignKey(Department,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=200)
    Phone=models.BigIntegerField()
    age=models.PositiveIntegerField()
    Qualification=models.CharField(max_length=200) 
    


 