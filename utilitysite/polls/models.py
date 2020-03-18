from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_access = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=False)

class UserConnections(models.Model):
    user_connection_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    connection_id = models.ForeignKey('Connection', on_delete=models.CASCADE)

class Connection(models.Model):
    connection_id = models.AutoField(primary_key=True)
    connection_name = models.CharField(max_length=100)
    connection_string = models.CharField(max_length=150)
    path = models.CharField(max_length=200)
    access_token = models.CharField(max_length=150)
    connection_cert = models.CharField(max_length=150)

