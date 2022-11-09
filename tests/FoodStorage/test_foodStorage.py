import unittest
from src.Food.food import Food
from src.FoodStorage.foodStorage import FoodStorage

class Test_FoodStorage(unittest.TestCase):
    food1 = Food("apple", "2022-11-08", 3)
    food2 = Food("pear", "2022-11-10", 3)
    food3 = Food("banana", "2022-11-06", 2)

    def setUp(self):
        self.foodStorage = FoodStorage()

    def testInitializeFoodStorage(self):
        self.assertFalse(self.foodStorage.isOpen)
        self._checkEmptyInventory()

    ''' Asserts that our current inventory is empty. '''
    def _checkEmptyInventory(self):
        self.assertEquals([], self.foodStorage.list())

    ''' Adds multiple foods into our food storage. '''
    def _addMultipleFoods(self):
        self.foodStorage.addFoods([self.food1, self.food2, self.food3])

    def testAddFoods(self):
        # Inventory should start as empty
        self._checkEmptyInventory()

        # Inventory should be sorted after adding multiple foods
        self._addMultipleFoods()
        self.assertEquals(
            [("2022-11-06", self.food3), ("2022-11-08", self.food1), ("2022-11-10", self.food2)], 
            self.foodStorage.list()
            )

        # Adding a new food, after listing, should still return a sorted inventory.
        self.foodStorage.add(self.food1)
        self.assertEquals(
            [("2022-11-06", self.food3), ("2022-11-08", self.food1), ("2022-11-08", self.food1), ("2022-11-10", self.food2)], 
            self.foodStorage.list()
            )

if __name__ == '__main__':
    unittest.main()