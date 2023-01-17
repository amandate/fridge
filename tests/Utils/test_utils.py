from src.Constants.constants import NEW_LINE
from src.Utils.utils import *
from tests.TestUtils.constants import \
    name1, \
    name2, \
    name3, \
    nameFuture, \
    nameNearFuture, \
    nameToday, \
    profile_name, \
    foodstorage_name

import io
import sys
import unittest

class Test_Utils(unittest.TestCase):
    def testListInQuotes(self):
        expected = ""
        self.assertEqual(expected, listInQuotes([]))

        expected = "'apple'"
        self.assertEqual(expected, listInQuotes([name1]))

        expected = "'apple', 'pear'"
        self.assertEqual(expected, listInQuotes([name1, name2]))

    def testListSepByTab(self):
        expected = ""
        self.assertEqual(expected, listSepByTab([]))

        expected = "apple"
        self.assertEqual(expected, listSepByTab([name1]))

        expected = "apple    pear"
        self.assertEqual(expected, listSepByTab([name1, name2]))

    def testTwoPrintOutcomes(self):
        arrayNegOutcome = []

        arrayPosOutcome = [name1, name2]

        posOutcome = [name3, nameToday]
        negOutcome = [nameNearFuture, nameFuture]

        suggestedActions = [profile_name, foodstorage_name]

        ## Negative outcome ##
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        actualOutcome = twoPrintOutcomes(arrayNegOutcome, posOutcome, negOutcome, suggestedActions)
        expectedPrint = nameNearFuture + SPACE + nameFuture + NEW_LINE + \
            SUGGESTED_ACTIONS_MESSAGE.format(f"'{profile_name}', '{foodstorage_name}'") + NEW_LINE
        self.assertEqual(expectedPrint, capturedPrintOutput.getvalue())
        self.assertFalse(actualOutcome)

        sys.stdout = sys.__stdout__

        ## Positive outcome ##
        capturedPrintOutput = io.StringIO()
        sys.stdout = capturedPrintOutput

        actualOutcome = twoPrintOutcomes(arrayPosOutcome, posOutcome, negOutcome, suggestedActions)
        expectedPrint = name3 + SPACE + nameToday + NEW_LINE + \
            name1 + TAB + name2 + NEW_LINE
        self.assertEqual(expectedPrint, capturedPrintOutput.getvalue())
        self.assertTrue(actualOutcome)

        sys.stdout = sys.__stdout__