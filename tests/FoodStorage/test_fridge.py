from src.Constants.messages import *
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
        self.assertEquals(dateToday, self.fridge.current_date)
        self.assertTrue(isEmptyInventory(self.fridge))

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # Inventory should be sorted after adding multiple foods
        self.fridge.addFoods([food1, food2, food3])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.fridge.list()
            )

        # Adding new food, after listing, should still return a sorted inventory.
        self.fridge.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2), 
            (dateToday, foodToday), (dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.fridge.list()
            )

    def testRemoveFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # At this point, PQ and _sortedList are empty and _stagedForRemoval has items
        self.fridge.removeFoods([food1, food3])
        self.assertEquals([], self.fridge.list())

        # At this point, PQ has items, _sortedList is empty, and _stagedForRemoval has items
        self.fridge.addFoods([food1, food2, food3, foodYesterday])
        self.fridge.removeFoods([food1, food3])
        self.assertEquals([(fooddate2, food2), (dateYesterday, foodYesterday)], self.fridge.list())

        # At this point, PQ is empty but _sortedList and _stagedForRemoval have items
        self.fridge.remove(food2)
        self.assertEquals([(dateYesterday, foodYesterday)], self.fridge.list())

        # At this point, PQ, _sortedList, and _stagedForRemoval have items
        self.fridge.addFoods([foodFuture, foodTomorrow, foodToday])
        self.fridge.removeFoods([foodToday, foodYesterday])
        self.assertEquals(
            [(dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.fridge.list())

    def testList(self):
        self.assertTrue(isEmptyInventory(self.fridge))

        self.fridge.addFoods(
            [foodFuture, foodTomorrow, foodNearFuture, foodToday, foodPast, foodYesterday])

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.assertEquals(
            [(dateMultDaysPassed, foodPast), (dateYesterday, foodYesterday), (dateToday, foodToday),
             (dateTomorrow, foodTomorrow), (dateWithinRange, foodNearFuture), (dateOutsideRange, foodFuture)], 
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
        self.assertEquals(expectedListOutput, actualListOutput)

        sys.stdout = sys.__stdout__

    def testOpen(self):
        self.assertFalse(self.fridge.isOpen)

        self.fridge.open()
        self.assertTrue(self.fridge.isOpen)

if __name__ == '__main__':
    unittest.main()