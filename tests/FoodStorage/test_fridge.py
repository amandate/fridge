import unittest
from src.FoodStorage.fridge import Fridge
from tests.Utilities.constants import *
from tests.Utilities.utils import *

class Test_Fridge(unittest.TestCase):
    def setUp(self):
        self.fridge = Fridge()

    def testInitializeFridge(self):
        self.assertFalse(self.fridge.isOpen)
        self.assertEquals(dateToday, self.fridge.current_day)
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

        # Adding new food, after listing, should still return a sorted inventory.
        self.fridge.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2), 
            (dateToday, foodToday), (dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.fridge.list()
            )

    def testOpen(self):
        self.assertFalse(self.fridge.isOpen)

        self.fridge.open()
        self.assertTrue(self.fridge.isOpen)

if __name__ == '__main__':
    unittest.main()