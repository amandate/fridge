from src.Constants.constants import EXPIRATION_DATE, EXPIRATION_WINDOW, FOOD, NAME, USE_BY_DATE
from src.Constants.foodStorage_messages import *
from src.FoodStorage.foodStorage import FoodStorage
from tests.TestUtils.constants import *
from tests.TestUtils.utils import *

import io
import sys
import unittest

class Test_FoodStorage(unittest.TestCase):
    def setUp(self):
        self.foodStorage = FoodStorage()

    def testInitializeFoodStorage(self):
        self.assertFalse(self.foodStorage.isOpen)
        self.assertEqual(dateToday, self.foodStorage.current_date)
        self.assertTrue(isEmptyInventory(self.foodStorage))
        self.assertEqual(7, self.foodStorage.expiration_window.days)

        self.foodStorage = FoodStorage(expiration_window=8)
        self.assertFalse(self.foodStorage.isOpen)
        self.assertEqual(dateToday, self.foodStorage.current_date)
        self.assertTrue(isEmptyInventory(self.foodStorage))
        self.assertEqual(8, self.foodStorage.expiration_window.days)

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # Inventory should be sorted after adding multiple foods
        self.foodStorage.addFoods([food1, food2, food3])
        self.assertEqual([food3, food1, food2], self.foodStorage.list())

        # Adding new food, after listing, should still return a sorted inventory.
        self.foodStorage.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEqual(
            [food3, food1, food2, foodToday, foodTomorrow, foodFuture], 
            self.foodStorage.list()
            )

    def testRemoveFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput


        self.foodStorage.remove(name1)

        self.assertEqual(f"{REMOVE_FOOD_FAILURE_MESSAGE.format(name1)}\n", capturedListOutput.getvalue())
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # reset standout
        sys.stdout = sys.__stdout__

        self.foodStorage.addFoods([food1, food2, food3])
        self.foodStorage.removeFoods([name1, name2])
        self.assertEqual([food3], self.foodStorage.list())

    def testList(self):
        self.assertTrue(isEmptyInventory(self.foodStorage))

        self.foodStorage.addFoods(
            [foodFuture, foodTomorrow, foodNearFuture, foodToday, foodPast, foodYesterday])

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.assertEqual(
            [foodPast, foodYesterday, foodToday, foodTomorrow, foodNearFuture, foodFuture], 
            self.foodStorage.list()
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
        self.assertFalse(self.foodStorage.isOpen)

        self.foodStorage.open()
        self.assertTrue(self.foodStorage.isOpen)

    def testUpdateFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # Update nonexistent foods
        self.foodStorage.updateFoods([name1, name3])
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # Update food that's there
        self.foodStorage.addFoods([food1, food2])
        self.assertEqual([food1, food2], self.foodStorage.list())

        self.foodStorage.update(name1)
        self.assertEqual([food2, food1], self.foodStorage.list())
    
    def testAsDictionary(self):
        ## Saves food storages as a dictionary without foods ##
        actual = self.foodStorage.asDictionary() 
        expected = {
            EXPIRATION_WINDOW : 7,
            FOOD : [],
        } 
        self.assertEqual(expected, actual)

        ## Saves food storages as a dictionary w/ foods ##
        self.foodStorage.addFoods([food1])
        actual = self.foodStorage.asDictionary() 
        expected = {
            EXPIRATION_WINDOW : 7,
            FOOD : [{
                NAME : name1,
                EXPIRATION_DATE : "2022-11-08",
                USE_BY_DATE : 3
            }]
        } 
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()