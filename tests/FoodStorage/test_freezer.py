from src.Constants.foodStorage_messages import *
from src.FoodStorage.freezer import Freezer
from tests.TestUtils.constants import *
from tests.TestUtils.utils import *

import io
import sys
import unittest

class Test_Freezer(unittest.TestCase):
    def setUp(self):
        self.freezer = Freezer()

    def testInitializeFreezer(self):
        self.assertFalse(self.freezer.isOpen)
        self.assertEqual(dateToday, self.freezer.current_date)
        self.assertTrue(isEmptyInventory(self.freezer))
        self.assertEqual(7, self.freezer.expiration_window.days)

        self.freezer = Freezer(expiration_window=8)
        self.assertFalse(self.freezer.isOpen)
        self.assertEqual(dateToday, self.freezer.current_date)
        self.assertTrue(isEmptyInventory(self.freezer))
        self.assertEqual(8, self.freezer.expiration_window.days)

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.freezer))

        # Inventory should be sorted after adding multiple foods
        self.freezer.addFoods([food1, food2, food3])
        self.assertEqual([food3, food1, food2], self.freezer.list())


        # Adding new food, after listing, should still return a sorted inventory.
        self.freezer.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEqual(
            [food3, food1, food2, foodToday, foodTomorrow, foodFuture], 
            self.freezer.list()
            )

    def testRemoveFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.freezer))

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput


        self.freezer.remove(name1)

        self.assertEqual(f"{REMOVE_FOOD_FAILURE_MESSAGE.format(name1)}\n", capturedListOutput.getvalue())
        self.assertTrue(isEmptyInventory(self.freezer))

        # reset standout
        sys.stdout = sys.__stdout__

        self.freezer.addFoods([food1, food2, food3])
        self.freezer.removeFoods([name1, name2])
        self.assertEqual([food3], self.freezer.list())


    def testList(self):
        self.assertTrue(isEmptyInventory(self.freezer))

        self.freezer.addFoods(
            [foodFuture, foodTomorrow, foodNearFuture, foodToday, foodPast, foodYesterday])

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.assertEqual(
            [foodPast, foodYesterday, foodToday, foodTomorrow, foodNearFuture, foodFuture], 
            self.freezer.list()
            )

        expectedListOutput = \
            f"{foodPast.name} {dateMultDaysPassed} {FOOD_EXPIRED_MESSAGE.format(2)}\n" + \
            f"{foodYesterday.name} {dateYesterday} {FOOD_EXPIRED_MESSAGE_SINGULAR}\n" + \
            f"{foodToday.name} {dateToday} {FOOD_EXPIRED_TODAY_MESSAGE}\n" + \
            f"{foodTomorrow.name} {dateTomorrow} {FOOD_ABOUT_TO_EXPIRE_MESSAGE_SINGULAR}\n" + \
            f"{foodNearFuture.name} {dateWithinRange} {FOOD_ABOUT_TO_EXPIRE_MESSAGE.format(2)}\n" + \
            f"{foodFuture.name} {dateOutsideRange} \n"

        actualListOutput = capturedListOutput.getvalue()
        self.assertEqual(expectedListOutput, actualListOutput)

        # reset standout
        sys.stdout = sys.__stdout__

    def testOpen(self):
        self.assertFalse(self.freezer.isOpen)

        self.freezer.open()
        self.assertTrue(self.freezer.isOpen)

    def testUpdateFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.freezer))

        # Update nonexistent foods
        self.freezer.updateFoods([name1, name3])
        self.assertTrue(isEmptyInventory(self.freezer))

        # Update food that's there
        self.freezer.addFoods([food1, food2])
        self.assertEqual([food1, food2], self.freezer.list())

        self.freezer.update(name1)
        self.assertEqual([food2, food1], self.freezer.list())

if __name__ == '__main__':
    unittest.main()