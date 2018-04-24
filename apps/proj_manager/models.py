from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=32)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    title = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    description = models.CharField(max_length=128)

    proj = models.ForeignKey(Project, related_name= 'tasks_of', on_delete=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

