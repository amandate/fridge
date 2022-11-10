import unittest
from src.Food.food import Food
from src.FoodStorage.freezer import Freezer

class Test_Freezer(unittest.TestCase):
    food1 = Food("apple", "2022-11-08", 3)
    food2 = Food("pear", "2022-11-10", 3)
    food3 = Food("banana", "2022-11-06", 2)

    def setUp(self):
        self.freezer = Freezer()

    def testInitializeFreezer(self):
        self.assertFalse(self.freezer.isOpen)

if __name__ == '__main__':
    unittest.main()