import unittest
from src.Food.food import Food
from src.FoodStorage.foodStorage import FoodStorage

class Test_FoodStorage(unittest.TestCase):

    def setUp(self):
        self.foodStorage = FoodStorage()
        self.food = Food("apple", "2022-11-08", 3)

    def testInitializeFoodStorage(self):
        self.assertFalse(self.foodStorage.isOpen)

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertEquals([], self.foodStorage.list())

        # Inventory should be sorted after adding multiple foods
        food2 = Food("pear", "2022-11-10", 3)
        food3 = Food("banana", "2022-11-06", 2)
        self.foodStorage.addFoods([self.food, food2, food3])
        print(self.foodStorage.list())
        self.assertEquals(
            [("2022-11-06", food3), ("2022-11-08", self.food), ("2022-11-10", food2)], 
            self.foodStorage.list()
            )

        # Adding a new food, after listing, should still return a sorted inventory.
        self.foodStorage.add(self.food)
        self.assertEquals(
            [("2022-11-06", food3), ("2022-11-08", self.food), ("2022-11-08", self.food), ("2022-11-10", food2)], 
            self.foodStorage.list()
            )

if __name__ == '__main__':
    unittest.main()