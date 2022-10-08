import unittest
from freezer import Freezer

class TestFreezer(unittest.TestCase):

    def testInitializeFreezer(self):
        freezer = Freezer()
        self.assertFalse(freezer.isOpen)

if __name__ == '__main__':
    unittest.main()