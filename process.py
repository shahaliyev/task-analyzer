import pandas as pd


essential_cols = [
    'title', 'category', 'urgency', 'priority', 
    'difficulty', 'hours', 'status', 'deadline']


def lower_df(tasks_df):
    tasks_df = tasks_df.copy(deep=True)
    
    for col in tasks_df.columns:
        if col != 'hours' and col != 'deadline':
            tasks_df[col] = tasks_df[col].str.lower()

    return tasks_df
    

def calc_days_left(tasks_df):
    # error check for timestamp format
    days_left = []
    for deadline in tasks_df['deadline']:     
        diff = (deadline - pd.to_datetime('today')) / pd.Timedelta(1, 'D')
        days_left.append(round(diff))
    
    return days_left


def process_df(tasks_df):
    tasks_df = tasks_df.copy(deep=True)

    tasks_df.columns = tasks_df.columns.str.lower()

    try:
        tasks_df = tasks_df[essential_cols]
    except:
        print('Data doesn\'t have all the essential columns:')
        print(essential_cols)

    tasks_df = lower_df(tasks_df)

    tasks_df['days_left'] = calc_days_left(tasks_df)

    return tasks_df