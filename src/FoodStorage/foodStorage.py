from queue import PriorityQueue

class FoodStorage:
    def __init__(self):
        self.isOpen = False
        self.__inventory__ = PriorityQueue()

    ''' Adds each food item from list_of_foods to self.__inventory__ '''
    def addFoods(self, list_of_foods):
        for food in list_of_foods:
            self.add(food)
        print("Successfully added all foods: ${list_of_foods}")

    ''' Adds food item to Food Storage. '''
    def add(self, food):
        date = food.expiration_date
        self.__inventory__.put((date, food))

    def remove(self, food):
        return

    def list(self):
        return list(self.__inventory__)
    
    def update(self, food):
        return