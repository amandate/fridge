import unittest
from fridge import Fridge

class TestFridge(unittest.TestCase):

    def testInitializeFridge(self):
        fridge = Fridge()
        self.assertFalse(fridge.isOpen)

if __name__ == '__main__':
    unittest.main()