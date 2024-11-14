# portfolio/models.py

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
   

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Collaboration(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Technology(models.Model):  
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name