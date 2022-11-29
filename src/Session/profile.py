from datetime import date
from src.Constants.keys import *

class Profile:
    def __init__(self, name):
        self.name = name
        self.current_date = date.today()
        self.foodStorages = {}

    def load(self, name):
        pass

    def save(self):
        pass