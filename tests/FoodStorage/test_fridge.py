import unittest
from src.FoodStorage.fridge import Fridge

class Test_Fridge(unittest.TestCase):

    def testInitializeFridge(self):
        fridge = Fridge()
        self.assertFalse(fridge.isOpen)

if __name__ == '__main__':
    unittest.main()