from rest_framework import seriealizers
from .models import Subject, Schedule


class SubjectSerializer(seriealizers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['owner', 'title', 'week_hours']


class ScheduleSerializer(seriealizers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['owner', 'week_day', 'time', 'subject']
