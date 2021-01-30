from functools import reduce
import math


def join_week_days(availabilities):
    week_availabilities = {}
    for availability in availabilities:
        if availability['weekday'] in week_availabilities:
            week_availabilities[availability['weekday']] += ([None] * availability['duration'])
        else:
            week_availabilities[availability['weekday']] = [None] * availability['duration']

    return week_availabilities


def prioritize_days(week_slots):
    info = []
    for week_day, slots in week_slots.items():
        ocup_slots = len(list(filter(lambda slot: slot is not None, slots)))
        avail_slots = len(slots) - ocup_slots
        info.append({
            'day': week_day,
            'business_p': 1 / (ocup_slots + 1),
            'available_p': avail_slots
        })

    info.sort(reverse=True, key=lambda k: (k['business_p'], k['available_p']))
    return [info_i['day'] for info_i in info]


def distribute_by_days(demand, days):
    remaining = demand
    distribution = [0] * min(demand, days)

    for i in range(0, len(distribution)):
        d_i = math.ceil(remaining / (days - i))
        distribution[i] = d_i
        remaining -= d_i

    return distribution


def is_enough_time(subjects, availabilities):
    total_hours_needed = 0

    for subject in subjects:
        total_hours_needed += subject['hours']

    hours_available = reduce( (lambda x, y: x + y['duration']), availabilities, 0)
    return hours_available >= total_hours_needed


def insert_in_slots(subject, sessions, preference, wd_slots):
    for i, session_duration in enumerate(sessions):
        day = preference[i]
        first_disponibility = 0
        for j, slot in enumerate(wd_slots[day]):
            if slot == None:
                first_disponibility = j
                break
        
        final = first_disponibility + session_duration
        wd_slots[day][first_disponibility:final] = [subject] * session_duration
    
    return wd_slots

# ###############
# v MAIN METHOD v
def create_schedule(subjects, availabilities):
    """
    subjects: [{title (string), hours (int)}],
    availabilities: [{weekday (int), duration (int)}]
    
    The hours needed are weekly.
    Weekday is 1 for Sunday, 2 for Monday, and so on.
    The start_time is measured in minutes since midnight.
    Duration is measured in hours

    Returns a schedule.
    """
    if not is_enough_time(subjects, availabilities):
        raise Exception(
            "Available time not enough"
        )

    index = 0
    max_index = len(subjects)
    
    sessions_by_wd = join_week_days(availabilities)
    
    subjects_ordered = subjects
    subjects_ordered.sort(reverse=True, key=lambda k: k['hours'])

    for subject in subjects_ordered:
        days_available = len(list(slots for day, slots in sessions_by_wd.items() if None in slots))
        sessions = distribute_by_days(subject['hours'], days_available)
        day_preference = prioritize_days(sessions_by_wd)
        sessions_by_wd = insert_in_slots(subject['title'], sessions, day_preference, sessions_by_wd)
    
    return sessions_by_wd


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

schedule = create_schedule(subjects, availabilities)