import unittest
from src.FoodStorage.foodStorage import FoodStorage
from tests.Utilities.constants import *
from tests.Utilities.utils import *

class Test_FoodStorage(unittest.TestCase):
    def setUp(self):
        self.foodStorage = FoodStorage()

    def testInitializeFoodStorage(self):
        self.assertFalse(self.foodStorage.isOpen)
        self.assertEquals(dateToday, self.foodStorage.current_day)
        self.assertTrue(isEmptyInventory(self.foodStorage))

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # Inventory should be sorted after adding multiple foods
        addMultipleFoods(self.foodStorage, [food1, food2, food3])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.foodStorage.list()
            )

        # Adding new food, after listing, should still return a sorted inventory.
        self.foodStorage.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2), 
            (dateToday, foodToday), (dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.foodStorage.list()
            )

    def testOpen(self):
        self.assertFalse(self.foodStorage.isOpen)

        self.foodStorage.open()
        self.assertTrue(self.foodStorage.isOpen)
        
if __name__ == '__main__':
    unittest.main()