import unittest
from datetime import date, timedelta
from src.Food.food import Food

class Test_Food(unittest.TestCase):
   
    def setUp(self):
        self.food = Food("apple", "2022-05-04", 2)

    def testInitializeFood(self):
        self.assertEqual("apple", self.food.name)
        self.assertEqual(date(2022, 5, 4), self.food.expiration_date)
        self.assertEqual(timedelta(days = 2), self.food.use_by_date)
        self.assertFalse(self.food.isOpen)  
    
    def testOpenFoods(self): 
        # Checks the initial value of isOpen, food should not be open yet.
        self.assertFalse(self.food.isOpen)

        # Opens food and updates expiration_date to new use_by_date. 
        self.food.open()
        self.assertEqual(date.today() + timedelta(days = 2), self.food.expiration_date)
        self.assertTrue(self.food.isOpen)

if __name__ == '__main__':
    unittest.main()