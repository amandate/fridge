from src.Constants.messages import *
from src.FoodStorage.foodStorage import FoodStorage
from tests.Utilities.constants import *
from tests.Utilities.utils import *

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

    def testAddFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # Inventory should be sorted after adding multiple foods
        self.foodStorage.addFoods([food1, food2, food3])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2)], 
            self.foodStorage.list()
            )

        # Adding new food, after listing, should still return a sorted inventory.
        self.foodStorage.addFoods([foodFuture, foodTomorrow, foodToday])
        self.assertEquals(
            [(fooddate3, food3), (fooddate1, food1), (fooddate2, food2), 
            (dateToday, foodToday), (dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.foodStorage.list()
            )

    def testRemoveFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # At this point, PQ and _sortedList are empty and _stagedForRemoval has items
        self.foodStorage.removeFoods([name1, name3])
        self.assertEquals([], self.foodStorage.list())

        # At this point, PQ has items, _sortedList is empty, and _stagedForRemoval has items
        self.foodStorage.addFoods([food1, food2, food3, foodYesterday])
        self.foodStorage.removeFoods([name1, name3])
        self.assertEquals([(fooddate2, food2), (dateYesterday, foodYesterday)], self.foodStorage.list())

        # At this point, PQ is empty but _sortedList and _stagedForRemoval have items
        self.foodStorage.remove(name2)
        self.assertEquals([(dateYesterday, foodYesterday)], self.foodStorage.list())

        # At this point, PQ, _sortedList, and _stagedForRemoval have items
        self.foodStorage.addFoods([foodFuture, foodTomorrow, foodToday])
        self.foodStorage.removeFoods([nameToday, nameYesterday])
        self.assertEquals(
            [(dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.foodStorage.list())

    def testList(self):
        self.assertTrue(isEmptyInventory(self.foodStorage))

        self.foodStorage.addFoods(
            [foodFuture, foodTomorrow, foodNearFuture, foodToday, foodPast, foodYesterday])

        # Grab print output from calling list()
        capturedListOutput = io.StringIO()
        sys.stdout = capturedListOutput

        self.assertEquals(
            [(dateMultDaysPassed, foodPast), (dateYesterday, foodYesterday), (dateToday, foodToday),
             (dateTomorrow, foodTomorrow), (dateWithinRange, foodNearFuture), (dateOutsideRange, foodFuture)], 
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
        self.assertEquals(expectedListOutput, actualListOutput)

        sys.stdout = sys.__stdout__

    def testOpen(self):
        self.assertFalse(self.foodStorage.isOpen)

        self.foodStorage.open()
        self.assertTrue(self.foodStorage.isOpen)

    def testUpdateFoods(self):
        # Inventory should start as empty
        self.assertTrue(isEmptyInventory(self.foodStorage))

        # PQ, _sortedList, _stagedForRemoval are empty
        # _stagedForUpdate has items
        self.foodStorage.updateFoods([name1, name3])
        self.assertEquals([], self.foodStorage.list())

        # PQ has items
        # _sortedList and _stagedForRemoval are empty
        # _stagedForUpdate has items
        self.foodStorage.addFoods([food1, food2])
        self.foodStorage.update(name1)
        self.assertEquals([(fooddate2, food2), (fooddate1, food1)], self.foodStorage.list())

        # PQ is empty
        # _sortedList has items
        # _stagedForRemoval is empty
        # _stagedForUpdate has items
        self.foodStorage.update(name2)
        self.assertEquals([(dateYesterday, foodYesterday)], self.foodStorage.list())

        # At this point, PQ, _sortedList, and _stagedForRemoval have items
        self.foodStorage.addFoods([foodFuture, foodTomorrow, foodToday])
        self.foodStorage.removeFoods([nameToday, nameYesterday])
        self.assertEquals(
            [(dateTomorrow, foodTomorrow), (dateOutsideRange, foodFuture)], 
            self.foodStorage.list())
        
if __name__ == '__main__':
    unittest.main()