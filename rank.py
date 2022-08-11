from score import score

def sort_dict(dictionary, descend=True):
    return {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=descend)}


def rank(tasks, descend=True, verbose=True):
    ranking = {}
    for task in tasks:
        ranking[task['title']] = score(task)
    
    ranking = sort_dict(ranking, descend=descend)

    if verbose:
        for k, v in ranking.items():
            print(k, v)

    return ranking
