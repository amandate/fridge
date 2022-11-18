from datetime import date
from src.Session.profile import Profile

import unittest

class Test_FoodStorage(unittest.TestCase):
    def setUp(self):
        self.profile = Profile("test")

    def testInitializeFoodStorage(self):
        self.assertEqual("test", self.profile.name)
        self.assertEqual(date.today(), self.profile.current_date)
        self.assertEqual({}, self.profile.foodStorages)


if __name__ == '__main__':
    unittest.main()