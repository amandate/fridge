from src.Constants.messages import *
from datetime import date, timedelta

class FoodStorage:
    def __init__(self, expiration_window=7):
        self.current_date = date.today()

        # Timeframe (in days) we consider important to note when listing foods.
        # By default, we highlight foods that will expire 7 days from now.
        self.expiration_window = timedelta(days=expiration_window)
        self.isOpen = False

        self._inventory = {}
        self._sortedInventory = []
        self._hasUpdates = False

    ''' Adds food item to self._inventoryPQ. '''
    def add(self, food):
        self._hasUpdates = True
        self._inventory[food.name] = food

    ''' Adds each food item from list_of_foods to self._inventoryPQ '''
    def addFoods(self, list_of_foods):
        for food in list_of_foods:
            self.add(food)
        print(ADD_FOODS_SUCCESS_MESSAGE.format(list_of_foods))

    def remove(self, food):
        return

    ''' Gets the notice message for a food that's about to expire or is expired. '''
    def _getExpirationNotice(self, expiration_date):
        if self._isWithinExpirationWindow(expiration_date):
            remaining_days = (expiration_date - self.current_date).days
            if remaining_days == 1:
                return FOOD_ABOUT_TO_EXPIRE_MESSAGE_SINGULAR
            elif remaining_days == -1:
                return FOOD_EXPIRED_MESSAGE_SINGULAR
            elif remaining_days > 0:
                return FOOD_ABOUT_TO_EXPIRE_MESSAGE.format(remaining_days)
            elif remaining_days < 0:
                return FOOD_EXPIRED_MESSAGE.format(-1 * remaining_days)
            else:
                return FOOD_EXPIRED_TODAY_MESSAGE
        return EMPTY_MESSAGE

    ''' Returns True if the expiration_date is within our expiration_window and False
        otherwise. In other words, returns whether something is going to expire
        self.expiration_window days from self.current_date. '''
    def _isWithinExpirationWindow(self, expiration_date):
        a = self.current_date + self.expiration_window
        return expiration_date < self.current_date + self.expiration_window

    ''' Prints self._sortedInventory to user.'''
    def _printList(self):
        for food in self._sortedInventory:
            notice = self._getExpirationNotice(food.expiration_date)
            print(f"{food.name} {food.expiration_date} {notice}")

    ''' Updates self._sortedInventory. If there were new foods added, since we last 
        updated our self._sortedInventory, we add everything from the current 
        self._sortedInventory into self._inventoryPQ and use it to repopulate 
        self._sortedInventory_. '''
    def _sortInventory(self):
        if self._hasUpdates:
            self._sortedInventory = sorted(self._inventory.values())
            self._hasUpdates = False


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
        self.current_date = date.today()
        self.list()
    
    def update(self, foodName):
        if foodName in self._inventory:
            prevFood = self._inventory[foodName]

            self._hasUpdates = True
            newFood = self._inventory[foodName].open()
            UPDATE_FOODS_SUCCESS_MESSAGE.format(prevFood, newFood)
        else:
            UPDATE_FOODS_FAILURE_MESSAGE.format(foodName)

    def updateFoods(self, list_of_food_names):
        for food in list_of_food_names:
            self.update(food)