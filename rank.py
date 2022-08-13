from score import score
from utils import sort_tasks

def rank(tasks, reverse=True, verbose=True):
    for task in tasks: 
        task.score = score(task)

    sort_tasks(tasks, 'score', reverse=reverse)

    for rank, task in enumerate(tasks, start=1):
        task.rank = rank
        if verbose:
            print(f'{rank}: {task.title} {task.score}')
