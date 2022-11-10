import unittest
from src.FoodStorage.foodStorage import FoodStorage
from tests.Utilities.constants import *
from tests.Utilities.utils import *

class Test_FoodStorage(unittest.TestCase):
    def setUp(self):
        self.foodStorage = FoodStorage()

    def testInitializeFoodStorage(self):
        self.assertFalse(self.foodStorage.isOpen)
        self._checkEmptyInventory()

    ''' Asserts that our current inventory is empty. '''
    def _checkEmptyInventory(self):
        self.assertEquals([], self.foodStorage.list())

    def testAddFoods(self):
        # Inventory should start as empty
        self._checkEmptyInventory()

        # Inventory should be sorted after adding multiple foods
        addMultipleFoods()
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.foodStorage.list()
            )

        # Adding a new food, after listing, should still return a sorted inventory.
        self.foodStorage.add(food1)
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate1, food1), (fooddate2, food2)], 
            self.foodStorage.list()
            )

if __name__ == '__main__':
    unittest.main()