from src.Session.session import Session
from src.Constants.constants import \
    EMPTY_STRING, \
    EXIT, \
    JSON_EXTENSION, \
    PROFILES_PATH, \
    TAB_STRING
from src.Constants.session_messages import *
from unittest.mock import patch

import unittest

class Test_Session(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    @patch('src.Session.session.input', create=True)
    def testStart(self, mocked_input):
        # TODO: This can't be tested right now until we implement _redirect
        pass