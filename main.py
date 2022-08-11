import pandas as pd
from rank import rank
from process import process_df
from tasks import create_task_dicts

# python 3.10.1
# pandas 1.3.5
# openpyxl 3.0.10

# Suggested tasks for today?
# Which tasks should be completed within the next 10 days?
# The ranking of the tasks
# Achievement badges?
# Reading list
# Top 10 challenging tasks
# Top 10 urgent tasks
# Most important tasks
# Which tasks to discard?
# Completed tasks
# Ongoing tasks
# New task to tackle?

if __name__ == '__main__': 
    tasks_df = pd.read_excel('files/Tasks.xlsx')
    tasks_df = process_df(tasks_df)
    tasks = create_task_dicts(tasks_df)
    ranking = rank(tasks)








    