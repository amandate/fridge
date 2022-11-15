from datetime import date, timedelta

class Food(object):
    def __init__(self, name, expiration_date, use_by_date):
        self.name = name
        self.expiration_date = date.fromisoformat(expiration_date)
        
        # use_by_date indicates the amount of time (in days) a food's quality will deteriorate after it is opened
        self.use_by_date = timedelta(days = use_by_date)
        self.isOpen = False
    
    '''Updates self.expiration_date to the current date plus self.use_by_date and updates self.isOpen. '''
    def open(self):
        if not self.isOpen:
            self.expiration_date = date.today() + self.use_by_date
            self.isOpen = True
        