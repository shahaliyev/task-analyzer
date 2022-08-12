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
        self.title = title.capitalize()
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

        self.score = nan
        self.rank = nan

        self.passed_deadline = self.days_left < 0
        self.discard = self.passed_deadline or (self.not_urgent and self.not_important) or self.score < 0

        self.issues = self.detect_issues()


    def calc_days_left(self):   
        return round((self.deadline - pd.to_datetime('today')) / pd.Timedelta(1, 'D'))

        
    def calc_hours_per_day(self):
        return round(self.hours / self.days_left, 1) if self.days_left > 0 else nan

    
    def __lt__(self, other):
        return self.score < other.score

    
    def info(self):
        info = ''
        info = info + f'The task is titled as "{self.title}".\n'
        info = info + f'Ranked {self.rank} with the score {self.score}.\n'
        info = info + f'{self.days_left} days till its deadline.\n'
        info = info + f'You need to spend about {self.hours_per_day} hours daily.\n'
        info = info + f'Its discard flag is {self.discard}.'

        return info


    def detect_issues(self):
        issues = ''

        if self.passed_deadline:
            issues = issues + f'Deadline has passed. It\'s been {abs(self.days_left)} days since the deadline.'

        if self.hours_per_day > 4:
            issues = issues + f'Too much daily effort ({self.hours_per_day} hours). Extend deadline, reconsider total hourly effort, or start working on the task more seriously.'

        if self.not_urgent and self.not_important:
            issues = issues + 'The task is not urgent and not important. Consider discarding the task.'

        if self.score < 0:
            issues = issues + 'Negative score. Seriously consider discarding the task.'

        return issues

        