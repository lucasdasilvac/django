from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=80)
    local = models.TextField()
    day = models.DateField()
    hour = models.TimeField()
    number_participants = models.IntegerField()

