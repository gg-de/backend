from rest_framework import seriealizers
from .models import Subject, Availability, Schedule


class SubjectSerializer(seriealizers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['owner', 'title', 'week_hours']


class AvailabilitySerializer(seriealizers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['owner', 'week_day', 'time']


class SubjectSerializer(seriealizers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['subject', 'time']
