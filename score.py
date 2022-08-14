from unicodedata import category

weights = {
    'urgency': 5,
    'priority': 4,
    'difficulty': 2,
}

points = {
    'high': 100,
    'medium': 50,
    'low': 10,
}

category_points = {
    'health': 200,
    'family': 200,
    'career': 150,
    'reading': 100,
}


deadline_points = {
    1: 500,
    3: 350,
    5: 250,
    10: 200,
    20: 100,
    30: 20,
}

daily_effort_points = {
    0.1: 30,
    0.5: 50,
    1: 100,
    3: 200,
    5: 300,
}


def get_deadline_point(task):
    for days in deadline_points.keys(): 
        if task.days_left <= days:
            return deadline_points[days]
    return 0


def get_daily_effort_point(task):
    for hours in daily_effort_points.keys(): 
        if task.hours_per_day <= hours:
            return daily_effort_points[hours]
    return 0


reverse_points = {
    'high': 10,
    'medium': 50,
    'low': 100,
}

def score(task):
    deadline_point = get_deadline_point(task)
    category_point = category_points.get(task.category, 0)
    daily_effort_point = get_daily_effort_point(task)

    urgency = points[task.urgency] * weights['urgency'] + deadline_point + daily_effort_point
    priority = points[task.priority] * weights['priority'] + category_point
    difficulty = points[task.difficulty] * weights['difficulty'] 

    return urgency + priority - difficulty