from django.db import models

# Create your models here.
class Subscriber_newsletter(models.Model):
    email=models.CharField(max_length=100)

class contact_us(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    review=models.CharField(max_length=500)