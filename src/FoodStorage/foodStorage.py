from queue import PriorityQueue
from datetime import date, timedelta

class FoodStorage:
    def __init__(self, expiration_window=7):
        self.isOpen = False
        self.current_day = date.today()
        self._inventoryPQ = PriorityQueue()
        self._sortedInventory = []

        # Timeframe (in days) we consider important to note when listing foods.
        # By default, we highlight foods that will expire 7 days from now.
        self.expiration_window = timedelta(days=expiration_window)

    ''' Adds each food item from list_of_foods to self._inventoryPQ '''
    def addFoods(self, list_of_foods):
        for food in list_of_foods:
            self.add(food)
        print(f"Successfully added all foods: {list_of_foods}")

    ''' Adds food item to self._inventoryPQ. '''
    def add(self, food):
        date = food.expiration_date
        self._inventoryPQ.put((date, food))

    def remove(self, food):
        return

    ''' Gets the notice message for a food that's about to expire or is expired. '''
    def _getExpirationNotice(self, expiration_date):
        remaining_days = (expiration_date - self.current_day).days
        if remaining_days > 0:
            return f" [{remaining_days} days until expired!]"
        elif remaining_days < 0:
            return f" [{-1 * remaining_days} days past expiration date!]"
        else:
            return " [Expires today! Last day to use this!]"

    ''' Returns True if the expiration_date is within our expiration_window and False
        otherwise. In other words, returns whether something is going to expire
        self.expiration_window days from self.current_day. '''
    def _isWithinExpirationWindow(self, expiration_date):
        a = self.current_day + self.expiration_window
        return expiration_date < self.current_day + self.expiration_window

    ''' Prints self._sortedInventory to user.'''
    def _printList(self):
        for expiration_date, food in self._sortedInventory:
            notice = self._getExpirationNotice(expiration_date) if self._isWithinExpirationWindow(expiration_date) else ""
            print(f"{food.name} {expiration_date}{notice}")

    ''' Updates self._sortedInventory. If there were new foods added, since we last 
        updated our self._sortedInventory, we add everything from the current 
        self._sortedInventory into self._inventoryPQ and use it to repopulate 
        self._sortedInventory_. '''
    def _sortInventory(self):
        if not self._inventoryPQ.empty():
            while self._sortedInventory:
                self._inventoryPQ.put(self._sortedInventory.pop())

            while not self._inventoryPQ.empty():
                self._sortedInventory.append(self._inventoryPQ.get())

    ''' Prints out a list of our inventory in order of earliest expiration date and also 
        returns the list in the form of an array. '''
    def list(self):
        self._sortInventory()
        self._printList()
        return self._sortedInventory

    ''' Represents opening the fridge and seeing it's contents. 
        This should give notice of what foods are going to expire in the specified time frame
        and list other foods in order of expiration_date. '''
    def open(self):
        if self.isOpen:
            return

        self.isOpen = True
        self.current_day = datetime.today()
        self.list()
    
    def update(self, food):
        return