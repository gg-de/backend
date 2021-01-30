from django.http import JsonResponse
from ggde.utils import create_schedule


def index(request):
    subjects = [
        {
            'title': 'Portugues',
            'hours': 2
        },
        {
            'title': 'Matematica',
            'hours': 2
        },
        {
            'title': 'Biologia',
            'hours': 1
        },
        {
            'title': 'Física',
            'hours': 3
        },
        {
            'title': 'Geografia',
            'hours': 1
        },
        {
            'title': 'Inglês',
            'hours': 1
        }
    ]

    availabilities = [
        {
            'weekday': 2,
            'duration': 3
        },
        {
            'weekday': 3,
            'duration': 3
        },
        {
            'weekday': 4,
            'duration': 2
        },
        {
            'weekday': 6,
            'duration': 3
        },
        {
            'weekday': 7,
            'duration': 3
        }
    ]

    timetable = create_schedule(subjects, availabilities)
    return JsonResponse(timetable)