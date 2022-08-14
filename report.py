from utils import create_df, get_discard_list, get_issues, get_urgent_tasks, get_reading_list, get_not_started_df
from rank import rank


def get_report(tasks):
    print('\n################## PROJECT REPORT ##################\n')
    rank(tasks, verbose=False)

    rank_attribs = ['title', 'score', 'days_left']
    ranked_df = create_df(tasks, attributes=rank_attribs, sort_by_attr='rank')  

    print_hr()
    print(f'TASK RANKINGS\n\n{ranked_df}\n')  

    print_hr()
    print('TASK ISSUES\n')
    get_issues(tasks, verbose=True)
    print()

    print_hr()
    print('TASKS TO DISCARD\n')
    print('Following tasks you may consider discarding:\n')
    for i, task_title in enumerate(get_discard_list(tasks), start=1):
        print(f'{i}. {task_title}')
    print()
    
    print_urgent_tasks(tasks)
    print_urgent_tasks(tasks, '3 days', 3)
    print_urgent_tasks(tasks, '10 days', 10)
    print_urgent_tasks(tasks, 'this month', 30)

    print_hr()
    print('NEW TASKS TO TACKLE\n')
    print('Following tasks you may want to start ASAP:\n')
    print(get_not_started_df(tasks))
    print()

    print_hr()
    print('READING LIST\n')
    for i, task_title in enumerate(get_reading_list(tasks), start=1):
        print(f'{i}. {task_title}')
    print()


def print_urgent_tasks(tasks, str='today', days=1, status='all'):
    print_hr()
    print(f'TASKS FOR {str.upper()}\n')
    if not get_urgent_tasks(tasks, days, status):
        print(f'No tasks for {str}.')
    print()


def print_hr():
     print('------------------------------')



