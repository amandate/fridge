from datetime import date, timedelta
from src.Food.food import Food
from tests.Utilities.constants import *

import unittest

class Test_Food(unittest.TestCase):
   
    def setUp(self):
        self.food = Food("apple", "2022-05-04", 2)

    def testInitializeFood(self):
        self.assertEqual("apple", self.food.name)
        self.assertEqual(date(2022, 5, 4), self.food.expiration_date)
        self.assertEqual(timedelta(days = 2), self.food.use_by_date)
        self.assertFalse(self.food.isOpen)  
    
    def testCompareFoods(self):
        self.assertLess(food1, food2) # date1 < date2
        self.assertLess(food1, food4) # date1 = date4
        self.assertLessEqual(food1, food4) # date1 = date4
        self.assertLessEqual(food1, food2) # date1 < date2
        self.assertEqual(food1, food5) # name1, date1 = name5, date5
        self.assertNotEqual(food1, food6) # name1 != name6, date1 = date6
        self.assertNotEqual(food1, food2) # name1 != name2, date1 != date 2
        self.assertGreaterEqual(food4, food1) # date4 = date1
        self.assertGreaterEqual(food2, food1) # date2 > date1
        self.assertGreater(food2, food1) # date2 > date1
        self.assertGreater(food4, food1) # date4 = date1

        actual = sorted([food1, food6, food3, food2, food5, food4])
        expected = [food3, food1, food5, food6, food4, food2]
        self.assertEqual(expected, actual)

    def testOpenFoods(self): 
        # Checks the initial value of isOpen, food should not be open yet.
        self.assertFalse(self.food.isOpen)

        # Opens food and updates expiration_date to new use_by_date. 
        self.food.open()
        self.assertEqual(date.today() + timedelta(days = 2), self.food.expiration_date)
        self.assertTrue(self.food.isOpen)

if __name__ == '__main__':
    unittest.main()