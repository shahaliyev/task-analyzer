import pandas as pd
from task import Task
from process import process_df


def get_task_list(tasks_df):
    tasks = tasks_df.values.tolist()
    return [Task(*task) for task in tasks]


def get_tasks_from_excel(filepath='files/Tasks.xlsx'):
    tasks_df = pd.read_excel(filepath)
    tasks_df = process_df(tasks_df)
    all_tasks = get_task_list(tasks_df)

    return all_tasks


def get_reading_list(tasks): 
    return [task.title.replace('Read ', '').capitalize() for task in tasks if task.category == 'reading']


def get_discard_list(tasks):
    return [task.title for task in tasks if task.discard]


def get_attributes(obj, type='dict'):
    if type == 'all':
        return dir(obj)
    elif type == 'dict':
        return list(obj.__dict__.keys())


def split_tasks(tasks):
    completed = [task for task in tasks if task.status == 'completed']
    not_completed = list(set(tasks) - set(completed))
    
    return not_completed, completed 


def check_attrib_error(obj, attribute):
    attributes = get_attributes(obj)
    if attributes.count(attribute) == 0:
        raise Exception(f'Incorrect attribute. Please choose one of the following: {attributes}')


def sort_tasks(tasks, attribute='score', reverse=False):
    check_attrib_error(tasks[0], attribute)
    return tasks.sort(key=lambda task: getattr(task, attribute), reverse=reverse)


def create_df(obj_list, attributes=None, sort_by_attr=None, reverse=False):
    attributes = get_attributes(obj_list[0]) if attributes is None else attributes
    sort_by_attr = attributes[0] if sort_by_attr is None else sort_by_attr

    [check_attrib_error(obj_list[0], attr) for attr in attributes]
    
    sort_tasks(obj_list, attribute=sort_by_attr, reverse=reverse)
    
    rows = []
    for obj in obj_list:
        row = [getattr(obj, attr) for attr in attributes]
        rows.append(row)

    df = pd.DataFrame(rows, columns=attributes)  
    df.index = df.index + 1

    return df



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

    if len(urgent_tasks) == 0:
        return None

    sort_tasks(urgent_tasks, 'days_left', reverse=reverse)

    if verbose:
        attributes = ['title', 'days_left', 'status', 'score', 'rank']
        df = create_df(urgent_tasks, attributes, 'days_left')
        print(df)

    return urgent_tasks


def get_issues(tasks, verbose=True):
    tasks_with_issues = [task for task in tasks if task.issues != '']

    sort_tasks(tasks_with_issues, 'deadline')

    if verbose:
        print(f'{len(tasks_with_issues)} tasks have issues:\n')
        for i, task in enumerate(tasks_with_issues, start=1):
            print(f'{i}. {task.title}')
        print()

        for task in tasks_with_issues:
            print(f'{task.title}: {task.issues}')

    return tasks_with_issues


def get_not_started_df(tasks):
    for days in range(20, 60):
        not_started = get_urgent_tasks(tasks, days, status='not started', verbose=False)
        if not_started:
            df = create_df(not_started, ['title', 'score', 'rank', 'days_left'], 'days_left')
            return df
