from django.db import models
from datetime import datetime

# Create your models here.
class Telecallers(models.Model):
  name = models.CharField(max_length=128)
  address = models.CharField(max_length=256)
  phone = models.IntegerField()
  email = models.CharField(max_length=50)
  dob = models.DateTimeField()
  sscname = models.CharField(max_length=128)
  sscpassyr = models.IntegerField()
  hscname = models.CharField(max_length=256)
  hscpassyr = models.IntegerField()
  diplname = models.CharField(max_length=256, blank=True)
  diplpassyr = models.IntegerField(blank=True)
  degname = models.CharField(max_length=256)
  degpassyr = models.IntegerField()
  masname = models.CharField(max_length=256, blank=True)
  maspassyr = models.IntegerField(blank=True)
  designation = models.CharField(max_length=128)
  passyr = models.IntegerField()
  expyr = models.IntegerField()
  expmon = models.IntegerField()
  date = models.DateTimeField(default=datetime.now)