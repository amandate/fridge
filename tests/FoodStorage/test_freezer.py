from src.Constants.messages import *
from src.FoodStorage.freezer import Freezer
from tests.Utilities.constants import *
from tests.Utilities.utils import *

import io
import sys
import unittest

class Test_Freezer(unittest.TestCase):
    def setUp(self):
        self.freezer = Freezer()

    def testInitializeFreezer(self):
        self.assertFalse(self.freezer.isOpen)
        self.assertEquals(dateToday, self.freezer.current_date)
        self.assertTrue(isEmptyInventory(self.freezer))

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.freezer))

        # Inventory should be sorted after adding multiple foods
        self.freezer.addFoods([food1, food2, food3])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.freezer.list()
            )

        # Adding new food, after listing, should still return a sorted inventory.
        self.freezer.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2), 
            (dateToday, foodToday), (dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.freezer.list()
            )

    def testList(self):
        self.assertTrue(isEmptyInventory(self.freezer))

        self.freezer.addFoods(
            [foodFuture, foodTomorrow, foodNearFuture, foodToday, foodPast, foodYesterday])

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.assertEquals(
            [(dateMultDaysPassed, foodPast), (dateYesterday, foodYesterday), (dateToday, foodToday),
             (dateTomorrow, foodTomorrow), (dateWithinRange, foodNearFuture), (dateOutsideRange, foodFuture)], 
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
        self.assertEquals(expectedListOutput, actualListOutput)

        sys.stdout = sys.__stdout__

    def testOpen(self):
        self.assertFalse(self.freezer.isOpen)

        self.freezer.open()
        self.assertTrue(self.freezer.isOpen)

    def testUpdateFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.freezer))

        # Grab print output from calling list()
        capturedUpdateOutput = io.StringIO()
        sys.stdout = capturedUpdateOutput

        # Update nonexistent foods
        self.freezer.updateFoods([name1, name3])
        expectedUpdateOutput = f"{UPDATE_FOODS_FAILURE_MESSAGE.format(name1)}\n" + \
                               f"{UPDATE_FOODS_FAILURE_MESSAGE.format(name3)}\n"
        self.assertEqual(expectedUpdateOutput, capturedUpdateOutput.getvalue())
        sys.stdout = sys.__stdout__ # reset standout
        self.assertTrue(isEmptyInventory(self.freezer))

        # Update food that's there
        self.freezer.addFoods([food1, food2])
        self.assertEqual([food1, food2], self.freezer.list())

        # Grab print output from calling list()
        capturedUpdateOutput = io.StringIO()
        sys.stdout = capturedUpdateOutput

        self.freezer.update(name1)
        expectedUpdateOutput = \
            f"{UPDATE_FOODS_SUCCESS_MESSAGE.format(food1, Food(name1, fooddate1open, 3))}\n"
        self.assertEqual(expectedUpdateOutput, capturedUpdateOutput.getvalue())
        self.assertEqual([food2, food1], self.freezer.list())
        sys.stdout = sys.__stdout__ # reset standout

if __name__ == '__main__':
    unittest.main()