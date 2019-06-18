from django.db import models
from api.models import User

class Profiles(models.Model):
    user = models.OneToOneField(
        'api.User', on_delete=models.CASCADE)
    location =models.CharField(max_length=255, blank=True)
    Contact =models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.user.username



