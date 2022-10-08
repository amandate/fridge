import unittest
from foodStorage import FoodStorage

class TestFoodStorage(unittest.TestCase):

    def testInitializeFoodStorage(self):
        foodStorage = FoodStorage()
        self.assertFalse(foodStorage.isOpen)

if __name__ == '__main__':
    unittest.main()