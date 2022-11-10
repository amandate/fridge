import unittest
from src.FoodStorage.foodStorage import FoodStorage

class Test_FoodStorage(unittest.TestCase):

    def testInitializeFoodStorage(self):
        foodStorage = FoodStorage()
        self.assertFalse(foodStorage.isOpen)

if __name__ == '__main__':
    unittest.main()