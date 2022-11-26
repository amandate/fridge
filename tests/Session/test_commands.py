from src.Session.commands import Commands
from unittest.mock import patch

import unittest

class Test_Commands(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()

    def testInitialize(self):
        self.assertIsNone(self.commands.profile)

    @patch('src.Session.commands.input', create=True)
    def testCreateProfile(self, mocked_input):
        # What we pass in for user input whenever input() is called
        mocked_input.side_effect = ["testProfile"]
        self.commands.create_profile()
        self.assertEqual("testProfile", self.commands.profile.name)

if __name__ == '__main__':
    unittest.main()