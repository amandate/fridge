from src.Session.commands import Commands

import unittest

class Test_Commands(unittest.TestCase):
    def setUp(self):
        self.commands = Commands()

    def get_input(text):
        return input(text)

    def testInitialize(self):
        self.assertIsNone(self.commands.profile)

    def testCreateProfile(self):
        self.commands.create_profile()
        self.assertEqual("testProfile", self.commands.profile.name)

if __name__ == '__main__':
    unittest.main()