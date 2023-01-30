from src.Session.commands import Commands
from src.Constants.commands_messages import \
    ADD_FOOD_ERROR_MESSAGE, \
    ADD_FOOD_SUCCESS_MESSAGE_FINAL, \
    CANCEL_ACTION_MESSAGE, \
    CREATE_FOOD_STORAGE_ACTION, \
    CREATE_FOOD_STORAGE_SUCCESS_MESSAGE, \
    INVALID_RESPONSE_MESSAGE, \
    LIST_FOOD_STORAGES_ACTION, \
    NO_FOOD_STORAGE_MESSAGE, \
    NO_LOADED_PROFILE_MESSAGE, \
    OPEN_FOOD_STORAGE_ACTION, \
    OPEN_FOOD_STORAGE_MESSAGE, \
    OPEN_FOOD_STORAGE_SUCCESS_MESSAGE, \
    SUGGESTED_ACTIONS_MESSAGE
from src.Constants.constants import *
from src.FoodStorage.foodStorage import FoodStorage
from src.Utils.utils import listInQuotes
from tests.TestUtils.constants import \
    date1, \
    date2, \
    foodstorage_name, \
    freezer_name, \
    fridge_name, \
    name1, \
    name2, \
    profile_name, \
    use_by_date1 
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
    def testAddFood(self, mocked_input):
        ## no profile ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.commands.add_food()

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + " " + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())
       
        # reset standout
        sys.stdout = sys.__stdout__

        ## Negative path: food storage not open ##
        mocked_input.side_effect = [profile_name]
        self.commands.create_profile()

        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        self.commands.add_food()

        expectedOutput = ADD_FOOD_ERROR_MESSAGE + NEW_LINE + \
            SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes([OPEN_FRIDGE, OPEN_FREEZER, CREATE_FREEZER, CREATE_FRIDGE])) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue()) 

        # reset standout
        sys.stdout = sys.__stdout__

        ## Success path: food storage exists, is open, 2 foods added ##
        mocked_input.side_effect = [freezer_name]
        self.commands.create_foodStorage(FREEZER)

        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        mocked_input.side_effect = [name1, date1, use_by_date1, YES, name2, date2, EMPTY_STRING, NO]
        self.commands.add_food()

        actualOutput = capturedPrintOutput.getvalue().strip().split(NEW_LINE)[-1]
        self.assertEqual(ADD_FOOD_SUCCESS_MESSAGE_FINAL, actualOutput)
    
        # reset standout
        sys.stdout = sys.__stdout__

        ## Success path: foods added w/ invalid response ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        mocked_input.side_effect = [name1, date1, use_by_date1, EXIT, NO]
        self.commands.add_food()

        output1 = capturedPrintOutput.getvalue().strip().split(NEW_LINE)[0]
        output2 = capturedPrintOutput.getvalue().strip().split(NEW_LINE)[-1]
        self.assertEqual(INVALID_RESPONSE_MESSAGE, output1)
        self.assertEqual(ADD_FOOD_SUCCESS_MESSAGE_FINAL, output2)

        # reset standout
        sys.stdout = sys.__stdout__

    @patch('src.Session.commands.input', create=True)
    def testCreateFoodStorage(self, mocked_input):
        ## no profile ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.commands.create_foodStorage(freezer_name)

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + " " + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())

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

        mocked_input.side_effect = [foodstorage_name, FREEZER, NO]
        self.commands.create_foodStorage(freezer_name)

        expectedOutput = \
            INVALID_RESPONSE_MESSAGE + NEW_LINE + \
            CANCEL_ACTION_MESSAGE.format(CREATE_FOOD_STORAGE_ACTION.format(freezer_name, foodstorage_name)) + NEW_LINE
        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## new food storage with existing name, yes ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = [foodstorage_name, YES]
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

    def testHelp(self):
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.commands.help()

        expectedOutput = \
            NEW_LINE.join([ADD_FOOD, CREATE_FREEZER, CREATE_FRIDGE, CREATE_PROFILE, DELETE_FOOD_STORAGE, 
                DELETE_FREEZER, DELETE_FRIDGE, DELETE_PROFILE, LIST_FOOD_STORAGES, LIST_FREEZERS, 
                LIST_FRIDGES, LOAD, OPEN_FOOD_STORAGE, OPEN_FREEZER, OPEN_FRIDGE, REMOVE_FOOD, SAVE]) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

    @patch('src.Session.commands.input', create=True)
    def testListFoodStorages(self, mocked_input):
        ## no profile ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.commands.list_food_storages(freezer_name)

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + " " + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())
       
        # reset standout
        sys.stdout = sys.__stdout__

        ## Postive outcome: lists existing food storages ##
        mocked_input.side_effect = [profile_name, freezer_name, freezer_name]
        self.commands.create_profile()
        self.commands.create_foodStorage(FREEZER)
        
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        self.commands.list_food_storages(FREEZER)

        expectedOutput = LIST_FOOD_STORAGES_ACTION.format(FREEZER) + NEW_LINE + freezer_name + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())
        
        # reset standout
        sys.stdout = sys.__stdout__

        ## Negative outcome: no food storage object of this type ##
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        self.commands.list_food_storages(FRIDGE)

        expectedOutput = NO_FOOD_STORAGE_MESSAGE.format(FRIDGE) + NEW_LINE + \
            SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes([CREATE_FOOD_STORAGE, CREATE_FREEZER, CREATE_FRIDGE])) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue()) 

        # reset standout
        sys.stdout = sys.__stdout__

    @patch('src.Session.commands.input', create=True)
    def testOpenFoodStorage(self, mocked_input):
        ## no profile ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.commands.open(freezer_name)

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + " " + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__
        
        ## Happy path: opens food storage with existing name ##
        mocked_input.side_effect = [profile_name, freezer_name, freezer_name]
        self.commands.create_profile()
        self.commands.create_foodStorage(FREEZER)
        
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        self.commands.open(FREEZER)

        expectedPosOutcome = OPEN_FOOD_STORAGE_MESSAGE.format(FREEZER) + NEW_LINE + freezer_name + NEW_LINE
        expectedOutput = expectedPosOutcome + \
            OPEN_FOOD_STORAGE_SUCCESS_MESSAGE.format(FREEZER, freezer_name) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())
        
        # reset standout
        sys.stdout = sys.__stdout__

        ## Negative outcome: no food storage object of this type ##
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        self.commands.open(FRIDGE)

        expectedOutput = NO_FOOD_STORAGE_MESSAGE.format(FRIDGE) + NEW_LINE + \
            SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes([CREATE_FOOD_STORAGE, CREATE_FREEZER, CREATE_FRIDGE])) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue()) 

        # reset standout
        sys.stdout = sys.__stdout__

        ## Food storage objects exist but food storage name does not exist, invalid response, cancel - NO ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = [fridge_name, FRIDGE, NO]
        self.commands.open(FREEZER)

        expectedOutput = expectedPosOutcome + \
            INVALID_RESPONSE_MESSAGE + NEW_LINE + \
            CANCEL_ACTION_MESSAGE.format(OPEN_FOOD_STORAGE_ACTION.format(FREEZER)) + NEW_LINE
        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

         # reset standout
        sys.stdout = sys.__stdout__

        ## Food storage objects exist but food storage name does not exist, create new food storage - YES ##
        # Grab print output from calling list
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = [fridge_name, YES, fridge_name]
        self.commands.open(FREEZER)

        expectedOutput = expectedPosOutcome + \
            CREATE_FOOD_STORAGE_SUCCESS_MESSAGE.format(FREEZER, fridge_name) + NEW_LINE

        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()