from django.db import models

# Create your models here.
class EntryURL(models.Model):
    URL = models.CharField(max_length=500, null=True)
    E1 = models.CharField(max_length=50, null=True)
    E1O = models.CharField(max_length=10, null=True)
    E2 = models.CharField(max_length=50, null=True)
    E2O = models.CharField(max_length=10, null=True)
    E3 = models.CharField(max_length=50, null=True)
    E3O = models.CharField(max_length=10, null=True)
    E4 = models.CharField(max_length=50, null=True)
    E4O = models.CharField(max_length=10, null=True)
    E5 = models.CharField(max_length=50, null=True)
    E5O = models.CharField(max_length=10, null=True)
    E6 = models.CharField(max_length=50, null=True)
    E6O = models.CharField(max_length=10, null=True)
    E7 = models.CharField(max_length=50, null=True)
    E7O = models.CharField(max_length=10, null=True)
    E8 = models.CharField(max_length=50, null=True)
    E8O = models.CharField(max_length=10, null=True)
    E9 = models.CharField(max_length=50, null=True)
    E9O = models.CharField(max_length=10, null=True)
    E10 = models.CharField(max_length=50, null=True)
    E10O = models.CharField(max_length=10, null=True)
    