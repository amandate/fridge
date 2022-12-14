from datetime import date
from src.Constants.constants import FREEZER, FRIDGE, FOOD_STORAGES
from src.FoodStorage.freezer import Freezer
from src.Session.profile import Profile
from tests.TestUtils.constants import profile_name, freezer_name, fridge_name

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
    
    def testOpen(self):
        # Should return 0 if there are no food storages.
        self.assertEqual(0, self.profile.open(FREEZER, freezer_name))

        # Should return 1 if a food storage exists.
        self.profile.addFoodStorage(FREEZER, freezer_name)
        self.assertEqual(1, self.profile.open(FREEZER, freezer_name))       

    def testListFoodStorages(self):
        # Should return an empty list if type does not exist. 
        self.assertEqual([], self.profile.listFoodStorages(FREEZER)) 

        # Should return list of food storages. 
        self.profile.addFoodStorage(FREEZER, freezer_name)
        self.assertEqual([freezer_name], self.profile.listFoodStorages(FREEZER)) 

        self.profile.addFoodStorage(FRIDGE, fridge_name)
        self.assertEqual([freezer_name, fridge_name], self.profile.listFoodStorages(FOOD_STORAGES)) 

if __name__ == '__main__':
    unittest.main()