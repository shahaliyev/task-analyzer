from cmath import nan
import pandas as pd


class Task:
    def __init__(
        self,
        title, 
        category, 
        urgency, 
        priority, 
        difficulty, 
        hours, 
        status, 
        deadline,
    ) -> None:
        self.title = title
        self.category = category
        self.urgency = urgency
        self.priority = priority
        self.difficulty = difficulty
        self.hours = hours
        self.status = status
        self.deadline = deadline

        self.not_urgent = self.urgency == 'low'
        self.not_important = self.priority == 'low'

        self.days_left = self.calc_days_left()
        self.hours_per_day = self.calc_hours_per_day()

        self.passed_deadline = self.days_left < 0
        self.discard = self.passed_deadline or (self.not_urgent and self.not_important)

        self.score = nan
        self.rank = nan


    def calc_days_left(self):   
        return round((self.deadline - pd.to_datetime('today')) / pd.Timedelta(1, 'D'))

        
    def calc_hours_per_day(self):
        return round(self.hours / self.days_left, 1) if self.days_left > 0 else nan

    
    def __lt__(self, other):
         return self.score < other.score

    
    def alarm(self):
        if self.passed_deadline:
            print(f'Deadline has passed. It\'s been {self.days_left} days since the deadline.')

        if self.hours_per_day > 4:
            print(f'Too much daily effort ({self.hours_per_day} hours). \
                Extend deadline, reconsider total hourly effort, \
                    or start working on the task more seriously.')

        if self.not_urgent and self.not_important:
            print('The task is not urgent and not important. Consider discarding the task.')

        if self.score < 0:
            print('Negative score. Consider discarding the task.')
        

