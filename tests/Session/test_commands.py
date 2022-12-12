from src.Session.commands import Commands
from src.Constants.commands_messages import \
    CANCEL_ACTION_MESSAGE, \
    CREATE_FREEZER_ACTION, \
    CREATE_FREEZER_SUCCESS_MESSAGE, \
    INVALID_RESPONSE_MESSAGE, \
    NO_LOADED_PROFILE_MESSAGE, \
    SUGGESTED_ACTIONS_MESSAGE
from src.Constants.constants import *
from src.FoodStorage.freezer import Freezer
from tests.TestUtils.constants import \
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
    def testCreateFreezer(self, mocked_input):
        ## no profile ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.commands.create_freezer()

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + " " + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + "\n"
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## happy path: new freezer ##
        mocked_input.side_effect = [profile_name, freezer_name]
        self.commands.create_profile()
        self.commands.create_freezer()
        freezer = self.commands.profile.getFoodStorage(FREEZER, freezer_name)
        self.assertIsNotNone(freezer)
        self.assertTrue(isinstance(freezer, Freezer))

        ## new freezer with existing name, invalid response, abort ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        mocked_input.side_effect = [freezer_name, "x", "n"]
        self.commands.create_freezer()

        expectedOutput = \
            INVALID_RESPONSE_MESSAGE + "\n" + \
            CANCEL_ACTION_MESSAGE.format(CREATE_FREEZER_ACTION.format(freezer_name)) + "\n"
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## new freezer with existing name, yes ##
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        mocked_input.side_effect = [freezer_name, "y"]
        self.commands.create_freezer()

        self.assertEqual(f"{CREATE_FREEZER_SUCCESS_MESSAGE.format(freezer_name)}\n", capturedPrintOutput.getvalue())

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
            NEW_LINE.join([ADD_FOOD, CREATE_FREEZER, CREATE_FRIDGE, CREATE_PROFILE, DELETE, DELETE_PROFILE, \
                LIST_FOOD_STORAGES, LIST_FREEZERS, LIST_FRIDGES, LOAD, OPEN, REMOVE_FOOD, SAVE]) + NEW_LINE
        self.assertEqual(expectedOutput, capturedPrintOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()