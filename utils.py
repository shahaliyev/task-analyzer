from task import Task


def get_task_list(tasks_df):
    tasks = tasks_df.values.tolist()
    return [Task(*task) for task in tasks]


def split_tasks(tasks):
    completed = [task for task in tasks if task.status == 'completed']
    not_completed = list(set(tasks) - set(completed))
    
    return not_completed, completed 


def get_reading_list(tasks): 
    return [task.title.replace('read ', '') for task in tasks if task.category == 'reading']


def get_discard_list(tasks):
    return [task.title for task in tasks if task.discard]