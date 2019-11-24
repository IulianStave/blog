from django.db import models
from django.contrib.auth.models import User

# Extend the existing user model that Django provide to add user picture
class Profile(models.Model):
    #associate a user to the profile
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'