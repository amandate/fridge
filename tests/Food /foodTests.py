import unittest
from food import Food

class TestFood(unittest.TestCase):
    def testInitializeFood(self):
        food = Food()
        food.activate()
        self.assertEquals(food.is_active())

if __name__ == '__main__':
    unittest.main()