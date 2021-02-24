from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe
# Create your models here.


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=43, default=token_urlsafe)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.createdAt} - {self.updatedAt} - {self.token}'
