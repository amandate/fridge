from datetime import date
from src.Constants.constants import FREEZER, FRIDGE, FOOD_STORAGE, PROFILES_PATH, SLASH, JSON_EXTENSION
from src.FoodStorage.freezer import Freezer
from src.Session.profile import Profile
from tests.TestUtils.constants import profile_name, freezer_name, fridge_name


import json 
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
        self.assertEqual([freezer_name, fridge_name], self.profile.listFoodStorages(FOOD_STORAGE)) 
    
    def testSave(self):
        # Profile with no food storages
        with open("tests/TestUtils/TestProfiles/profile_no_foodStorages.json") as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + "leeza" + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

        # Profile with one food storage ("fridge")
        with open("tests/TestUtils/TestProfiles/profile_fridge.json") as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + "amanda" + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

        # Profile with multiple food storages ("fridge" and "freezer")
        with open("tests/TestUtils/TestProfiles/profile_fridge_freezer.json") as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + "josh" + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

        ## will add later ##
        # # Profile with food storage and food objects
        # with open("tests/TestUtils/TestProfiles/profile_withFoods.json") as user_file:
        #     testProfile = json.load(user_file)
        # with open(PROFILES_PATH + SLASH + "sesame" + JSON_EXTENSION) as user_profile:
        #     savedProfile = json.load(user_profile)

        # self.assertEqual(testProfile, savedProfile)

if __name__ == '__main__':
    unittest.main()