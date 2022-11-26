from src.Constants.foodStorage_messages import *
from src.FoodStorage.fridge import Fridge
from tests.Utilities.constants import *
from tests.Utilities.utils import *

import io
import sys
import unittest

class Test_Fridge(unittest.TestCase):
    def setUp(self):
        self.fridge = Fridge()

    def testInitializeFridge(self):

        self.assertFalse(self.fridge.isOpen)
        self.assertEqual(dateToday, self.fridge.current_date)
        self.assertTrue(isEmptyInventory(self.fridge))
        self.assertEqual(7, self.fridge.expiration_window.days)

        self.fridge = Fridge(expiration_window=8)
        self.assertFalse(self.fridge.isOpen)
        self.assertEqual(dateToday, self.fridge.current_date)
        self.assertTrue(isEmptyInventory(self.fridge))
        self.assertEqual(8, self.fridge.expiration_window.days)

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # Inventory should be sorted after adding multiple foods
        self.fridge.addFoods([food1, food2, food3])
        self.assertEqual([food3, food1, food2], self.fridge.list())

        # Adding new food, after listing, should still return a sorted inventory.
        self.fridge.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEqual(
            [food3, food1, food2, foodToday, foodTomorrow, foodFuture], 
            self.fridge.list()
            )

    def testRemoveFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput


        self.fridge.remove(name1)

        self.assertEqual(f"{REMOVE_FOOD_FAILURE_MESSAGE.format(name1)}\n", capturedListOutput.getvalue())
        self.assertTrue(isEmptyInventory(self.fridge))

        # reset standout
        sys.stdout = sys.__stdout__

        self.fridge.addFoods([food1, food2, food3])
        self.fridge.removeFoods([name1, name2])
        self.assertEqual([food3], self.fridge.list())

    def testList(self):
        self.assertTrue(isEmptyInventory(self.fridge))

        self.fridge.addFoods(
            [foodFuture, foodTomorrow, foodNearFuture, foodToday, foodPast, foodYesterday])

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.assertEqual(
            [foodPast, foodYesterday, foodToday, foodTomorrow, foodNearFuture, foodFuture], 
            self.fridge.list()
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
        self.assertFalse(self.fridge.isOpen)

        self.fridge.open()
        self.assertTrue(self.fridge.isOpen)

    def testUpdateFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # Update nonexistent foods
        self.fridge.updateFoods([name1, name3])

        self.assertTrue(isEmptyInventory(self.fridge))

        # Update food that's there
        self.fridge.addFoods([food1, food2])
        self.assertEqual([food1, food2], self.fridge.list())

        self.fridge.update(name1)
        self.assertEqual([food2, food1], self.fridge.list())

if __name__ == '__main__':
    unittest.main()