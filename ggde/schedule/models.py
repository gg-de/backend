from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    week_hours = models.IntegerField(default=0)


class Availability(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weekday = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(1)])
    time = models.IntegerField(validators=[MaxValueValidator(23), MinValueValidator(0)])


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    time = models.ForeignKey(Availability, on_delete=models.CASCADE)