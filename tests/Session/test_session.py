from src.Session.session import Session
from src.Constants.session_messages import *
from unittest.mock import patch

import unittest

class Test_Session(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def testCommandWithoutProfile():

    @patch('src.Session.session.input', create=True)
    def testStart(self, mocked_input):
        # TODO: This can't be tested right now until we do regression tests
        # grab print output
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput
        mocked_input.side_effect = [profile_name, foodstorage_name]

        # reset standout
        sys.stdout = sys.__stdout__