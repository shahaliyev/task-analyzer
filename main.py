from utils import get_tasks_from_excel, split_tasks
from report import get_report


if __name__ == '__main__': 
    all_tasks = get_tasks_from_excel('./files/Tasks.xlsx')
    tasks, completed_tasks = split_tasks(all_tasks)
    get_report(tasks)

   













    