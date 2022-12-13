from src.Session.session import Session
from src.Constants.session_messages import *
from unittest.mock import patch

import unittest

class Test_Session(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    @patch('src.Session.session.input', create=True)
    def testStart(self, mocked_input):
        # TODO: This can't be tested right now until we do regression tests
        pass