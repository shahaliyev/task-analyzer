points = {
    'high': 1000,
    'medium': 100,
    'low': 10,
}

deadline_points = {
    3: 10000,
    10: 7000,
    20: 5000,
    30: 2000,
    60: 1000,
}


def score_deadline(days_left):
    for days in deadline_points.keys(): 
        if days_left <= days:
            return deadline_points[days]

    return 0
            

def score(task):
    urgency = task['urgency']
    priority = task['priority']
    difficulty = task['difficulty']

    days_left = task['days_left']

    a = points[urgency] * 5
    b = points[priority] * 4
    c = points[difficulty] * 2

    d = score_deadline(days_left)
    
    return a + b + c + d