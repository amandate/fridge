from datetime import date
from src.Constants.constants import FREEZER, FRIDGE, FOOD_STORAGE, PROFILES_PATH, SLASH, JSON_EXTENSION
from src.FoodStorage.freezer import Freezer
from src.Session.profile import Profile
from tests.TestUtils.constants import profile_name, freezer_name, fridge_name, food1


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

    def testGetOpenFoodStorage(self):
        # Should return None if food storage is not open. 
        self.assertIsNone(self.profile.getOpenFoodStorage())
       
        # Should return not none if food storage is open. 
        self.profile.addFoodStorage(FREEZER, freezer_name)
        freezer = self.profile.getOpenFoodStorage()
        self.assertIsNotNone(self.profile.getOpenFoodStorage())
        self.assertTrue(isinstance(freezer, Freezer))

    def testListFoodStorages(self):
        # Should return an empty list if type does not exist. 
        self.assertEqual([], self.profile.listFoodStorages(FREEZER)) 

        # Should return list of food storages. 
        self.profile.addFoodStorage(FREEZER, freezer_name)
        self.assertEqual([freezer_name], self.profile.listFoodStorages(FREEZER)) 

        self.profile.addFoodStorage(FRIDGE, fridge_name)
        self.assertEqual([freezer_name, fridge_name], self.profile.listFoodStorages(FOOD_STORAGE)) 
    
    def testSave(self):
        TEST_PROFILES_PATH = "tests/TestUtils/TestProfiles/"
        
        # Profile with no food storages
        TEST_PROFILE_NAME_1 = "leeza"
        PROFILE_NO_FOOD_STORAGES = "profile_no_foodStorages"
        profile1 = Profile(TEST_PROFILE_NAME_1)
        profile1.save()
        with open(TEST_PROFILES_PATH + PROFILE_NO_FOOD_STORAGES + JSON_EXTENSION) as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + TEST_PROFILE_NAME_1 + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

        # Profile with one food storage ("fridge")
        TEST_PROFILE_NAME_2 = "amanda"
        PROFILE_W_ONE_FOOD_STORAGE = "profile_fridge"
        profile2 = Profile(TEST_PROFILE_NAME_2)
        profile2.addFoodStorage(FRIDGE, fridge_name)
        profile2.save()
        with open(TEST_PROFILES_PATH + PROFILE_W_ONE_FOOD_STORAGE + JSON_EXTENSION) as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + TEST_PROFILE_NAME_2 + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

        # Profile with multiple food storages ("fridge" and "freezer")
        TEST_PROFILE_NAME_3 = "josh"
        PROFILE_W_MULTI_FOOD_STORAGE = "profile_fridge_freezer"
        profile3 = Profile(TEST_PROFILE_NAME_3)
        profile3.addFoodStorage(FRIDGE, fridge_name)
        profile3.addFoodStorage(FREEZER, freezer_name)
        profile3.save()
        with open(TEST_PROFILES_PATH + PROFILE_W_MULTI_FOOD_STORAGE + JSON_EXTENSION) as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + TEST_PROFILE_NAME_3 + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

        # Profile with food storage and food objects
        TEST_PROFILE_NAME_4 = "sesame"
        PROFILE_W_FOOD = "profile_withFoods"
        profile4 = Profile(TEST_PROFILE_NAME_4)
        profile4.addFoodStorage(FRIDGE, fridge_name)
        profile4.addFoodStorage(FREEZER, freezer_name)
        profile4.addFoods([food1])
        profile4.save()
        with open(TEST_PROFILES_PATH + PROFILE_W_FOOD + JSON_EXTENSION) as user_file:
            testProfile = json.load(user_file)
        with open(PROFILES_PATH + SLASH + TEST_PROFILE_NAME_4 + JSON_EXTENSION) as user_profile:
            savedProfile = json.load(user_profile)

        self.assertEqual(testProfile, savedProfile)

    def testAddFoods(self):
        # Should return 0 if food storage is not open yet.
        self.assertEqual(0, self.profile.addFoods([food1]))

        # Should return 1 if food item can be added. 
        self.profile.addFoodStorage(FREEZER, freezer_name)
        self.assertEqual(1, self.profile.addFoods([food1]))

if __name__ == '__main__':
    unittest.main()