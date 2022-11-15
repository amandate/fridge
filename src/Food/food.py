from datetime import date, timedelta

class Food(object):
    def __init__(self, name, expiration_date, use_by_length):
        self.name = name
        self.expiration_date = date.fromisoformat(expiration_date)
        self.use_by_length = timedelta(days = use_by_length)
        self.isOpen = False
    
    '''Updates self.expiration_date to self.use_by_length according to date food item is opened. 
        If date is changed, self.isOpen updates to True.'''
    def open(self):
        if not self.isOpen:
            self.expiration_date = date.today() + self.use_by_length
            self.isOpen = True
        