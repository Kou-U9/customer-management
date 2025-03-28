from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ScreenPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screen_name = models.CharField(max_length=100)
    can_access = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.screen_name}"