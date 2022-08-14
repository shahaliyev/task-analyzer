from utils import get_tasks_from_excel, split_tasks
from report import get_report
import sys, os


if __name__ == '__main__': 
    filepath = os.path.join('./files', sys.argv[1])
    all_tasks = get_tasks_from_excel(filepath)
    tasks, completed_tasks = split_tasks(all_tasks)
    get_report(tasks)

   













    