from src.Session.commands import Commands
from src.Constants.commands_messages import \
    CANCEL_ACTION_MESSAGE, \
    CREATE_FOOD_STORAGE_ACTION, \
    CREATE_FOOD_STORAGE_SUCCESS_MESSAGE, \
    CREATE_PROFILE, \
    INVALID_RESPONSE_MESSAGE, \
    LOAD, \
    NO_LOADED_PROFILE_MESSAGE, \
    SUGGESTED_ACTIONS_MESSAGE
from src.Constants.constants import \
    FOOD_STORAGE
from src.FoodStorage.foodStorage import FoodStorage
from tests.Utilities.constants import \
    foodstorage_name, \
    freezer_name, \
    profile_name
from unittest.mock import patch

import io
import sys
import unittest

class Test_Commands(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()

    def testInitialize(self):
        self.assertIsNone(self.commands.profile)

    @patch('src.Session.commands.input', create=True)
    def testCreateFoodStorage(self, mocked_input):
        ## no profile ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.commands.create_foodStorage(freezer_name)

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + " " + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + "\n"
        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## happy path: new food storage ##
        mocked_input.side_effect = [profile_name, foodstorage_name]
        self.commands.create_profile()
        self.commands.create_foodStorage(freezer_name)
        foodStorage = self.commands.profile.getFoodStorage(freezer_name, foodstorage_name)
        self.assertIsNotNone(foodStorage)
        self.assertTrue(isinstance(foodStorage, FoodStorage))

        ## new food storage with existing name, invalid response, abort ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = [foodstorage_name, "x", "n"]
        self.commands.create_foodStorage(freezer_name)

        expectedOutput = \
            INVALID_RESPONSE_MESSAGE + "\n" + \
            CANCEL_ACTION_MESSAGE.format(CREATE_FOOD_STORAGE_ACTION.format(freezer_name, foodstorage_name)) + "\n"
        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## new food storage with existing name, yes ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = [foodstorage_name, "y"]
        self.commands.create_foodStorage(freezer_name)

        self.assertEqual(f"{CREATE_FOOD_STORAGE_SUCCESS_MESSAGE.format(freezer_name, foodstorage_name)}\n", capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__


    @patch('src.Session.commands.input', create=True)
    def testCreateProfile(self, mocked_input):
        # What we pass in for user input whenever input() is called
        mocked_input.side_effect = [profile_name]
        self.commands.create_profile()
        self.assertEqual(profile_name, self.commands.profile.name)

if __name__ == '__main__':
    unittest.main()