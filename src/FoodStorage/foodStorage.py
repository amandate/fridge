from queue import PriorityQueue

class FoodStorage:
    def __init__(self):
        self.isOpen = False
        self._inventoryPQ = PriorityQueue()
        self._sortedInventory = []

    ''' Adds each food item from list_of_foods to self._inventoryPQ '''
    def addFoods(self, list_of_foods):
        for food in list_of_foods:
            self.add(food)
        print("Successfully added all foods: ${list_of_foods}")

    ''' Adds food item to self._inventoryPQ. '''
    def add(self, food):
        date = food.expiration_date
        self._inventoryPQ.put((date, food))

    def remove(self, food):
        return

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

    ''' Lists our inventory in order of earliest expiration date. '''
    def list(self):
        self._sortInventory()
        return self._sortedInventory
    
    def update(self, food):
        return