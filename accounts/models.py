from django.db import models
from django.contrib.auth.models import User

# Create your models here.

select_package = (
    ('1', 'Gold'),
    ('2', 'Silver'),
    ('3', 'Platinum'),
)


class Pakage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pakage = models.CharField(max_length=100, choices=select_package)
