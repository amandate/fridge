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

    def testUpdateFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.fridge))

        # Grab print output from calling list()
        capturedUpdateOutput = io.StringIO()
        sys.stdout = capturedUpdateOutput

        # Update nonexistent foods
        self.fridge.updateFoods([name1, name3])
        expectedUpdateOutput = f"{UPDATE_FOODS_FAILURE_MESSAGE.format(name1)}\n" + \
                               f"{UPDATE_FOODS_FAILURE_MESSAGE.format(name3)}\n"
        self.assertEqual(expectedUpdateOutput, capturedUpdateOutput.getvalue())
        sys.stdout = sys.__stdout__ # reset standout
        self.assertTrue(isEmptyInventory(self.fridge))

        # Update food that's there
        self.fridge.addFoods([food1, food2])
        self.assertEqual([food1, food2], self.fridge.list())

        # Grab print output from calling list()
        capturedUpdateOutput = io.StringIO()
        sys.stdout = capturedUpdateOutput

        self.fridge.update(name1)
        expectedUpdateOutput = \
            f"{UPDATE_FOODS_SUCCESS_MESSAGE.format(food1, Food(name1, fooddate1open, 3))}\n"
        self.assertEqual(expectedUpdateOutput, capturedUpdateOutput.getvalue())
        self.assertEqual([food2, food1], self.fridge.list())
        sys.stdout = sys.__stdout__ # reset standout

if __name__ == '__main__':
    unittest.main()