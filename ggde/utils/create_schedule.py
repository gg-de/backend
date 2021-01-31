import math


def join_week_days(availabilities):
    week_availabilities = {
        'sunday': [],
        'monday': [],
        'tuesday': [],
        'wednesday': [],
        'thursday': [],
        'friday': [],
        'saturday': []
    }
    for availability in availabilities:
        week_availabilities[availability['weekday']] += [{'subject': None, 'time': availability['time']}]

    return week_availabilities


def prioritize_days(week_slots):
    info = []
    for week_day, slots in week_slots.items():
        ocup_slots = len(list(filter(lambda slot: slot['subject'] is not None, slots)))
        avail_slots = len(slots) - ocup_slots
        if avail_slots == 0:
            info.append({
                'day': week_day,
                'business_p': 0,
                'available_p': 0
            })
        else:
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

    hours_available = len(availabilities)
    return hours_available >= total_hours_needed


def insert_in_slots(subject, sessions, preference, wd_slots):
    for i, session_duration in enumerate(sessions):
        day = preference[i]
        first_disponibility = 0
        for j, slot in enumerate(wd_slots[day]):
            if slot['subject'] == None:
                first_disponibility = j
                break
        
        final = first_disponibility + session_duration

        for time in range(first_disponibility, final):
            wd_slots[day][time]['subject'] = subject
        # wd_slots[day][first_disponibility:final] = [{'subject': subject}] * session_duration
    
    return wd_slots

# ###############
# v MAIN METHOD v
def create_schedule(subjects, availabilities):
    """
    subjects: [{title (string), hours (int)}],
    availabilities: [{weekday (int), time (int)}]
    
    The hours needed in subject are weekly.
    Weekday is 1 for Sunday, 2 for Monday, and so on.
    The time is measured in hours since midnight.

    Returns a schedule: {
        sunday: [{subject: (string), time(int)}],
        monday: ...
        # and so on for each day on week
        # empty days will be empty arrays
    }.
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
        days_available = len(list(
            slots for day, slots in sessions_by_wd.items() if any(slot['subject'] == None for slot in slots)
        ))
        sessions = distribute_by_days(subject['hours'], days_available)
        day_preference = prioritize_days(sessions_by_wd)
        sessions_by_wd = insert_in_slots(subject['title'], sessions, day_preference, sessions_by_wd)
    
    print(sessions_by_wd)
    return sessions_by_wd


# Dev test data:
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
    }
]

availabilities = [
        {
            "weekday": "monday",
            "time": 15
        },
        {
            "weekday": "monday",
            "time": 16
        },
        {
            "weekday": "tuesday",
            "time": 16
        },
        {
            "weekday": "tuesday",
            "time": 17
        },
        {
            "weekday": "friday",
            "time": 14
        },
        {
            "weekday": "friday",
            "time": 15
        },
        {
            "weekday": "friday",
            "time": 16
        }
    ]

# schedule = create_schedule(subjects, availabilities)