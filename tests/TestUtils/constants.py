from src.Food.food import Food
from datetime import date, timedelta

timedelta1 = timedelta(days=1)
timedelta2 = timedelta(days=2)
timedelta8 = timedelta(days=8)

name1 = "apple"
name2 = "pear"
name3 = "banana"
nameToday = "grape"
nameTomorrow = "curry"
nameYesterday = "beef"
namePast = "noodles"
nameNearFuture = "lettuce"
nameFuture = "meat"

date1 = "2022-11-08"
date2 = "2022-11-10"

fooddate1 = date.fromisoformat(date1)
fooddate2 = date.fromisoformat(date2)
fooddate3 = date(2022, 11, 6)
dateToday = date.today()
fooddate1open = dateToday + timedelta(3)
dateTomorrow = dateToday + timedelta1
dateYesterday = dateToday - timedelta1
dateMultDaysPassed = dateToday - timedelta2
dateWithinRange = dateToday + timedelta2
dateOutsideRange = dateToday + timedelta8

use_by_date1 = "3"

food1 = Food(name1, fooddate1.isoformat(), int(use_by_date1))
food2 = Food(name2, fooddate2.isoformat(), 3)
food3 = Food("banana", fooddate3.isoformat(), 2)
food4 = Food("soda", fooddate1.isoformat(), 3)
food5 = Food("apple", fooddate1.isoformat(), 3)
foodToday = Food("grape", dateToday.isoformat(), 2)
foodTomorrow = Food("curry", dateTomorrow.isoformat(), 2)
foodYesterday = Food("apricots", dateYesterday.isoformat(), 4)
foodPast = Food("noodles", dateMultDaysPassed.isoformat(), 3)
foodNearFuture = Food("lettuce", dateWithinRange.isoformat(), 7)
foodFuture = Food("meat", dateOutsideRange.isoformat(), 5)

profile_name = "testProfile"
foodstorage_name = "testFoodStorage"
freezer_name = "testFreezer"
fridge_name = "testFridge"