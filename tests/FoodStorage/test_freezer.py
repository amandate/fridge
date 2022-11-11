import unittest
from src.FoodStorage.freezer import Freezer
from tests.Utilities.constants import *
from tests.Utilities.utils import *

class Test_Freezer(unittest.TestCase):
    def setUp(self):
        self.freezer = Freezer()

    def testInitializeFreezer(self):
        self.assertFalse(self.freezer.isOpen)
        self.assertTrue(isEmptyInventory(self.freezer))

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.freezer))

        # Inventory should be sorted after adding multiple foods
        addMultipleFoods(self.freezer, [food1, food2, food3])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.freezer.list()
            )

        # Adding a new food, after listing, should still return a sorted inventory.
        self.freezer.add(food1)
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate1, food1), (fooddate2, food2)], 
            self.freezer.list()
            )


if __name__ == '__main__':
    unittest.main()