from statistics import mode
from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # link to abother model 
    title = models.CharField(max_length=200) # limit the num of characters
    text = models.TextField() # no limit for text
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        # get string with post title 
        return self.title

"""
Create tables for models in my database
1. make Django know we have some changes in model
python manage.py makemigrations blog
2. after Django create database for us, we have to apply it to our database 
python manage.py migrate blog
"""
