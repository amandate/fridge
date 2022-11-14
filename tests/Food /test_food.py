import unittest
from src.Food.food import Food

class Test_Food(unittest.TestCase):
   
    def testInitializeFood(self):
        food = Food("apple", "2022-5-4", 2)
        self.assertEqual("apple", food.name)
        self.assertEqual("2022-5-4", food.expiration_date)
        self.assertEqual(2, food.use_by_length)
        self.assertFalse(self.food.isOpen) 
    
    def testOpenFoods(self):




if __name__ == '__main__':
    unittest.main()



#conduct tests for new function 