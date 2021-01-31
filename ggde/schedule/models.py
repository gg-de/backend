from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    week_hours = models.IntegerField(default=0)


class Schedule(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weekday = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(1)])
    time = models.IntegerField(validators=[MaxValueValidator(23), MinValueValidator(0)])
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
