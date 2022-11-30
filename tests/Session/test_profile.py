from datetime import date
from src.Constants.keys import FREEZER
from src.FoodStorage.freezer import Freezer
from src.Session.profile import Profile
from tests.Utilities.constants import profile_name, freezer_name

import unittest

class Test_Profile(unittest.TestCase):
    def setUp(self):
        self.profile = Profile(profile_name)

    def testInitialize(self):
        self.assertEqual(profile_name, self.profile.name)
        self.assertEqual(date.today(), self.profile.current_date)

    def testAddGetFoodStorage(self):
        # Starts off None
        freezer = self.profile.getFoodStorage(FREEZER, freezer_name)
        self.assertIsNone(freezer)

        # Should exist after adding
        self.profile.addFoodStorage(FREEZER, freezer_name)
        freezer = self.profile.getFoodStorage(FREEZER, freezer_name)
        self.assertIsNotNone(freezer)
        self.assertTrue(isinstance(freezer, Freezer))

        # Should not have freezer of different name
        freezer = self.profile.getFoodStorage(FREEZER, "dummy")
        self.assertIsNone(freezer)

if __name__ == '__main__':
    unittest.main()