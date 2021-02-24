from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=100)
    cvr = models.CharField(max_length=8)
    eu = models.BooleanField()
    relatedToUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.cvr} - {self.eu}'
