def create_task_dicts(tasks_df, task_count=None):
    '''Seperates each tasks and creates dictionaries 
    based on columns of the datafram'''
    
    if task_count is None:
        task_count = len(tasks_df.index)
    
    cols = tasks_df.columns.tolist()

    task_dicts = []
    for i in range(task_count):
        task = tasks_df.iloc[i].tolist()
        task_dict = dict(zip(cols, task))
        task_dicts.append(task_dict)

    return task_dicts