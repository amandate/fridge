import unittest
from src.FoodStorage.freezer import Freezer

class Test_Freezer(unittest.TestCase):

    def testInitializeFreezer(self):
        freezer = Freezer()
        self.assertFalse(freezer.isOpen)

if __name__ == '__main__':
    unittest.main()