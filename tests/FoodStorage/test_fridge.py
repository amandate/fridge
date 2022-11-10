import unittest
from src.FoodStorage.fridge import Fridge
from tests.Utilities.constants import *
from tests.Utilities.utils import *

class Test_Fridge(unittest.TestCase):
    def setUp(self):
        self.fridge = Fridge()

    ''' Asserts that our current inventory is empty. '''
    def _checkEmptyInventory(self):
        self.assertEquals([], self.foodStorage.list())

    def testInitializeFridge(self):
        self.assertFalse(self.fridge.isOpen)
        self.assertTrue(isEmptyInventory(self.fridge))

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # Inventory should be sorted after adding multiple foods
        addMultipleFoods(self.fridge, [food1, food2, food3])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.fridge.list()
            )

        # Adding a new food, after listing, should still return a sorted inventory.
        self.fridge.add(food1)
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate1, food1), (fooddate2, food2)], 
            self.fridge.list()
            )

if __name__ == '__main__':
    unittest.main()