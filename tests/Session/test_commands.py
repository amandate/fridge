from src.Session.commands import Commands
from src.Constants.commands_messages import \
    CANCEL_ACTION_MESSAGE, \
    CREATE_FREEZER_ACTION, \
    CREATE_FREEZER_SUCCESS_MESSAGE, \
    CREATE_PROFILE, \
    INVALID_RESPONSE_MESSAGE, \
    LOAD, \
    NO_LOADED_PROFILE_MESSAGE, \
    SUGGESTED_ACTIONS_MESSAGE
from src.Constants.keys import \
    FREEZER
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
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.commands.create_freezer()

        expectedOutput = \
            NO_LOADED_PROFILE_MESSAGE + "\n" + \
            SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)) + "\n"
        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## happy path: new freezer ##
        mocked_input.side_effect = ["testProfile", "testFreezer"]
        self.commands.create_profile()
        self.commands.create_freezer()
        self.assertIn("testFreezer", self.commands.profile.foodStorages[FREEZER])

        ## new freezer with existing name, invalid response, abort ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = ["testFreezer", "x", "n"]
        self.commands.create_freezer()

        expectedOutput = \
            INVALID_RESPONSE_MESSAGE + "\n" + \
            CANCEL_ACTION_MESSAGE.format(CREATE_FREEZER_ACTION.format("testFreezer")) + "\n"
        self.assertEqual(expectedOutput, capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__

        ## new freezer with existing name, yes ##
        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        mocked_input.side_effect = ["testFreezer", "y"]
        self.commands.create_freezer()

        self.assertEqual(f"{CREATE_FREEZER_SUCCESS_MESSAGE}\n", capturedListOutput.getvalue())

        # reset standout
        sys.stdout = sys.__stdout__


    @patch('src.Session.commands.input', create=True)
    def testCreateProfile(self, mocked_input):
        # What we pass in for user input whenever input() is called
        mocked_input.side_effect = ["testProfile"]
        self.commands.create_profile()
        self.assertEqual("testProfile", self.commands.profile.name)

if __name__ == '__main__':
    unittest.main()