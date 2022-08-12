from score import score

def rank(tasks, verbose=True):
    for task in tasks: 
        task.score = score(task)

    tasks.sort(reverse=True)

    for rank, task in enumerate(tasks, start=1):
        task.rank = rank
        if verbose:
            print(f'{rank}: {task.title} {task.score}')
