from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# Add a class Post that inherits models.Model
# auto_now = True for DateTimeField will set the date 
# when the post was created
"""
We use the User from django.contrib.auth to create 
the author as a ForeignKey 
"""


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    #dunder str method
    def __str__(self):
        return self.title

