import pandas as pd
from rank import rank
from process import process_df
from utils import *


if __name__ == '__main__': 
    tasks_df = pd.read_excel('files/Tasks.xlsx')
    tasks_df = process_df(tasks_df)
    all_tasks = get_task_list(tasks_df)
    tasks, completed_tasks = split_tasks(all_tasks)
    rank(tasks)
   
   













    