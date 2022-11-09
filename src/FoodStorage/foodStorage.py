from queue import PriorityQueue

class FoodStorage:
    def __init__(self):
        self.isOpen = False
        self.__inventoryPQ__ = PriorityQueue()
        self.__sortedInventory__ = []

    ''' Adds each food item from list_of_foods to self.__inventoryPQ__ '''
    def addFoods(self, list_of_foods):
        for food in list_of_foods:
            self.add(food)
        print("Successfully added all foods: ${list_of_foods}")

    ''' Adds food item to self.__inventoryPQ__. '''
    def add(self, food):
        date = food.expiration_date
        self.__inventoryPQ__.put((date, food))

    def remove(self, food):
        return

    ''' Updates self.__sortedInventory__. If there were new foods added, since we last 
        updated our self.__sortedInventory__, we add everything from the current 
        self.__sortedInventory__ into self.__inventoryPQ__ and use it to repopulate 
        self.__sortedInventory___. '''
    def __sortInventory__(self):
        if not self.__inventoryPQ__.empty():
            while self.__sortedInventory__:
                self.__inventoryPQ__.put(self.__sortedInventory__.pop())

            while not self.__inventoryPQ__.empty():
                self.__sortedInventory__.append(self.__inventoryPQ__.get())

    ''' Lists our inventory in order of earliest expiration date. '''
    def list(self):
        self.__sortInventory__()
        return self.__sortedInventory__
    
    def update(self, food):
        return