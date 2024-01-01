from django.db import models

# Create your models here.
class bloodbank(models.Model):
    bgroup = models.CharField(max_length = 4)
    quantity = models.IntegerField()
    donated_quantity = models.IntegerField()

class patients(models.Model):
    patient_name= models.CharField(max_length =50)
    gender = models.CharField(max_length =7)
    patient_bloodgroup = models.CharField(max_length =4)
    quantity = models.IntegerField()

class donors(models.Model):
    donor_name = models.CharField(max_length =50)
    gender = models.CharField(max_length =7)
    donor_bloodgroup = models.CharField(max_length =4)
    quantity = models.IntegerField()