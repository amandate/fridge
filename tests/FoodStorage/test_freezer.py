import unittest
from src.FoodStorage.freezer import Freezer
from tests.Utilities.constants import *
from tests.Utilities.utils import *

class Test_Freezer(unittest.TestCase):
    def setUp(self):
        self.freezer = Freezer()

    def testInitializeFreezer(self):
        self.assertFalse(self.freezer.isOpen)
        self.assertEquals(dateToday, self.freezer.current_day)
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

        # Adding new food, after listing, should still return a sorted inventory.
        self.freezer.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2), 
            (dateToday, foodToday), (dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.freezer.list()
            )

    def testOpen(self):
        self.assertFalse(self.freezer.isOpen)

        self.freezer.open()
        self.assertTrue(self.freezer.isOpen)


if __name__ == '__main__':
    unittest.main()