from utils import sort_tasks, create_df


def get_urgent_tasks(tasks, days=10, status='all', reverse=False, verbose=True):
    if status == 'all':
        statuses = ['ongoing', 'not started']
    elif status == 'ongoing' or status == 'not started':
        statuses = [status]
    else:
        raise Exception('Incorrect status. Choose between "ongoing" and "not started".')

    urgent_tasks = []
    for task in tasks:
        if task.days_left <= days and statuses.count(task.status):
            urgent_tasks.append(task)

    sort_tasks(urgent_tasks, 'days_left', reverse=reverse)

    if verbose:
        attributes = ['title', 'days_left', 'status', 'score']
        df = create_df(urgent_tasks, attributes, 'days_left')
        print(df)

    return urgent_tasks


