from django.db import models

# Create your models here.
class Transactions(models.Model):
    payer = models.CharField(max_length=50)
    points = models.IntegerField()
    timestamp = models.DateField()
    