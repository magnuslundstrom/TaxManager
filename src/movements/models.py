from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from companies.models import Company

# Create your models here.


class Movement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    partner = models.ForeignKey(Company, on_delete=models.CASCADE)
    invoiceLink = models.CharField(max_length=300, default='')
    createdAt = models.DateTimeField(default=now)

    def __str__(self):
        return f'amount: {self.amount} partner: {self.partner}'
