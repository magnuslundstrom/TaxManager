from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Movement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    sender = models.CharField(max_length=200, default='')
    receiver = models.CharField(max_length=200, default='')

    def __str__(self):
        return f'amount: {self.amount} - sender: {self.sender} - receiver: {self.receiver}'
