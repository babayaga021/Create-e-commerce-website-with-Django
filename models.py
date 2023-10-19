from django.db import models

# Create your models here.
class Contact(models.Models):
    name = models.CharField(max_Length=100)
    email = models.CharField(max_Length=100)
    phone = models.CharField(max_Length=12)
    desc = models.TextField()
    date = models.DateField()