from django.db import models


class ForecastDay:
    def __init__(self, date, max_temp, min_temp, condition, icon):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.condition = condition
        self.icon = icon
