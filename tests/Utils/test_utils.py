from src.Utils.utils import *
from tests.TestUtils.constants import \
    name1, \
    name2

import unittest

class Test_Utils(unittest.TestCase):
    def testListInQuotes(self):
        expected = ""
        self.assertEquals(expected, listInQuotes([]))

        expected = "'apple'"
        self.assertEquals(expected, listInQuotes([name1]))

        expected = "'apple', 'pear'"
        self.assertEquals(expected, listInQuotes([name1, name2]))

    def testListSepByTab(self):
        expected = ""
        self.assertEquals(expected, listSepByTab([]))

        expected = "apple"
        self.assertEquals(expected, listSepByTab([name1]))

        expected = "apple    pear"
        self.assertEquals(expected, listSepByTab([name1, name2]))