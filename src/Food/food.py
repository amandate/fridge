from datetime import date, timedelta
from src.Constants.constants import NAME, EXPIRATION_DATE, USE_BY_DATE


class Food(object):
    def __init__(self, name, expiration_date, use_by_date=None):
        self.name = name
        self.expiration_date = date.fromisoformat(expiration_date)
        
        if use_by_date:
            # use_by_date indicates the amount of time (in days) 
            # a food's quality will deteriorate after it is opened.
            self.use_by_date = timedelta(days = use_by_date)
        else:
            self.use_by_date = use_by_date
        self.isOpen = False

    ''' Following methods are comparators that will sort food items by expiration_date and name. 
        Returns self.expiration_date first if it has an earlier date than other.expiration_date. 
        If expiration_date's are equal, objects will be returned by name alphabetically. '''

    ''' Checks if self.expiration_date is earlier than other.expiration_date. 
        If expiration_date's are the same, sorts by name. '''
    def __lt__(self, other): 
        if self.expiration_date == other.expiration_date:
            return self.name < other.name
        return self.expiration_date < other.expiration_date
            
    ''' Checks if self.expiration_date is earlier than or the same as other.expiration_date. 
        If expiration_dates are the same, sorts by name. '''
    def __le__(self, other):
        if self.expiration_date == other.expiration_date:
            return self.name <= other.name
        return self.expiration_date <= other.expiration_date

    ''' Checks if self.name of food items are the same. '''
    def __eq__(self, other):
        return self.name == other.name

    ''' Checks if self.name of food items are not the same. '''
    def __ne__(self, other):
        return self.name != other.name

    ''' Checks if self.expiration_date is later than other.expiration_date. 
        If expiration_date's are the same, sorts by name. '''
    def __gt__(self, other):
        if self.expiration_date == other.expiration_date:
            return self.name > other.name
        return self.expiration_date > other.expiration_date

    ''' Checks if self.expiration_date is later than or the same as other.expiration_date.
        If expiration_date's are the same, sorts by name. '''
    def __ge__(self, other):
        if self.expiration_date == other.expiration_date:
            return self.name >= other.name
        return self.expiration_date >= other.expiration_date

    ''' Updates self.expiration_date to the current date plus self.use_by_date
        and updates self.isOpen. '''
    def open(self):
        if not self.isOpen:
            if self.use_by_date:
                self.expiration_date = date.today() + self.use_by_date
            self.isOpen = True
    
    ''' Compiles food objects into a dictionary. '''
    def asDictionary(self):
        food_dict = {
            NAME : self.name,
            EXPIRATION_DATE : self.expiration_date,
            USE_BY_DATE : self.use_by_date
        }
        return food_dict 