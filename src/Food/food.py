from datetime import date, timedelta

class Food(object):
    def __init__(self, name, expiration_date, use_by_date):
        self.name = name
        self.expiration_date = date.fromisoformat(expiration_date)
        
        # use_by_date indicates the amount of time (in days) a food's quality will deteriorate after it is opened
        self.use_by_date = timedelta(days = use_by_date)
        self.isOpen = False

    def __lt__(self, other): 
        if self.expiration_date == other.expiration_date:
            return self.name < other.name
        return self.expiration_date < other.expiration_date
            
    def __le__(self, other):
        if self.expiration_date == other.expiration_date:
            return self.name <= other.name
        return self.expiration_date <= other.expiration_date

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __gt__(self, other):
        if self.expiration_date == other.expiration_date:
            return self.name > other.name
        return self.expiration_date > other.expiration_date

    def __ge__(self, other):
        if self.expiration_date == other.expiration_date:
            return self.name >= other.name
        return self.expiration_date >= other.expiration_date

    '''Updates self.expiration_date to the current date plus self.use_by_date and updates self.isOpen. '''
    def open(self):
        if not self.isOpen:
            self.expiration_date = date.today() + self.use_by_date
            self.isOpen = True
    
