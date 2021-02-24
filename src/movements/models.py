from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Movement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    partner = models.CharField(max_length=200, default='')
    invoiceLink = models.CharField(max_length=300, default='')
    movementDate = models.CharField(max_length=20, default='')
    createdAt = models.DateTimeField(default=now)

    def __str__(self):
        return f'amount: {self.amount} partner: {self.partner}'
