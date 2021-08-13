from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional
    portfolia_site = models.URLField(blank=True, max_length=200)
    profile_pic = models.ImageField(
        upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
