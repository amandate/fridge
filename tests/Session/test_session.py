from src.Constants.commands_messages import INVALID_RESPONSE_MESSAGE  
from src.Constants.constants import \
    ADD_FOOD, \
    CREATE_FOOD_STORAGE, \
    CREATE_FREEZER, \
    CREATE_FRIDGE, \
    CREATE_PROFILE, \
    DELETE_FOOD_STORAGE, \
    DELETE_FREEZER, \
    DELETE_FRIDGE, \
    DELETE_PROFILE, \
    EXIT, \
    FOOD_STORAGE, \
    FREEZER, \
    FRIDGE, \
    HELP, \
    LIST_FOOD_STORAGES, \
    LIST_FREEZERS, \
    LIST_FRIDGES, \
    LOAD, \
    JSON_EXTENSION, \
    NEW_LINE, \
    OPEN_FOOD_STORAGE, \
    OPEN_FREEZER, \
    OPEN_FRIDGE, \
    REMOVE_FOOD, \
    SAVE
from src.Constants.session_messages import *
from src.Session.session import Session
from unittest.mock import patch

import sys, io
import unittest

class Test_Session(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    # Checks that the method located at method_path is called once with potential parameters
    # expected_args when the user provides input within side_effect.
    def checkCommandMethodCalled(self, mocked_input, side_effect, method_path, *expected_args):
        mocked_input.side_effect = side_effect
        with patch(method_path) as mock:
            self.session.start()
        mock.assert_called_once_with(*expected_args)

    @patch('src.Session.session.input', create=True)
    def testStart(self, mocked_input):
        # This skips checking the welcome message, since twoPrintOutcomes
        # has been tested in utils and it depends on someone's personal profiles.

        # Testing that the 'exit' command properly exits the program
        mocked_input.side_effect = [EXIT]
        self.session.start()
        self.assertRaises(SystemExit)

        # Testing that all commands redirect to their respective handlers in commands.py
        command_class_path = "src.Session.commands.Commands"
        self.checkCommandMethodCalled(mocked_input, [ADD_FOOD, EXIT], command_class_path + ".add_food")
        self.checkCommandMethodCalled(mocked_input, [CREATE_FOOD_STORAGE, EXIT], command_class_path + ".create_foodStorage", FOOD_STORAGE)
        self.checkCommandMethodCalled(mocked_input, [CREATE_FREEZER, EXIT], command_class_path + ".create_foodStorage", FREEZER)
        self.checkCommandMethodCalled(mocked_input, [CREATE_FRIDGE, EXIT], command_class_path + ".create_foodStorage", FRIDGE)
        self.checkCommandMethodCalled(mocked_input, [CREATE_PROFILE, EXIT], command_class_path + ".create_profile")
        self.checkCommandMethodCalled(mocked_input, [DELETE_FOOD_STORAGE, EXIT], command_class_path + ".delete", FOOD_STORAGE)
        self.checkCommandMethodCalled(mocked_input, [DELETE_FREEZER, EXIT], command_class_path + ".delete", FREEZER)
        self.checkCommandMethodCalled(mocked_input, [DELETE_FRIDGE, EXIT], command_class_path + ".delete", FRIDGE)
        self.checkCommandMethodCalled(mocked_input, [DELETE_PROFILE, EXIT], command_class_path + ".delete_profile")
        self.checkCommandMethodCalled(mocked_input, [HELP, EXIT], command_class_path + ".help")
        self.checkCommandMethodCalled(mocked_input, [LIST_FOOD_STORAGES, EXIT], command_class_path + ".list_food_storages", FOOD_STORAGE)
        self.checkCommandMethodCalled(mocked_input, [LIST_FREEZERS, EXIT], command_class_path + ".list_food_storages", FREEZER)
        self.checkCommandMethodCalled(mocked_input, [LIST_FRIDGES, EXIT], command_class_path + ".list_food_storages", FRIDGE)
        self.checkCommandMethodCalled(mocked_input, [LOAD, EXIT], command_class_path + ".load")
        self.checkCommandMethodCalled(mocked_input, [OPEN_FOOD_STORAGE, EXIT], command_class_path + ".open", FOOD_STORAGE)
        self.checkCommandMethodCalled(mocked_input, [OPEN_FREEZER, EXIT], command_class_path + ".open", FREEZER)
        self.checkCommandMethodCalled(mocked_input, [OPEN_FRIDGE, EXIT], command_class_path + ".open", FRIDGE)
        self.checkCommandMethodCalled(mocked_input, [REMOVE_FOOD, EXIT], command_class_path + ".remove_food")
        self.checkCommandMethodCalled(mocked_input, [SAVE, EXIT], command_class_path + ".save")

        # Testing that any other commands results in the INVALID_RESPONSE_MESSAGE
        mocked_input.side_effect = [JSON_EXTENSION, EXIT]

        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        self.session.start()

        actualPrintOutput = capturedPrintOutput.getvalue().strip().split(NEW_LINE)[-1]
        self.assertEqual(INVALID_RESPONSE_MESSAGE, actualPrintOutput)

        # reset standout
        sys.stdout = sys.__stdout__