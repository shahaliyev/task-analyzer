import pandas as pd
from task import Task


def get_task_list(tasks_df):
    tasks = tasks_df.values.tolist()
    return [Task(*task) for task in tasks]


def get_reading_list(tasks): 
    return [task.title.replace('read ', '') for task in tasks if task.category == 'reading']


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


def create_df(obj_list, attributes, sort_by_attr=None, reverse=False):
    [check_attrib_error(obj_list[0], attr) for attr in attributes]

    sort_by_attr = attributes[0] if sort_by_attr is None else sort_by_attr
    sort_tasks(obj_list, attribute=sort_by_attr, reverse=reverse)
    
    rows = []
    for obj in obj_list:
        row = [getattr(obj, attr) for attr in attributes]
        rows.append(row)

    return pd.DataFrame(rows, columns=attributes)
