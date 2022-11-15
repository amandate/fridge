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

fooddate1 = date(2022, 11, 8)
fooddate2 = date(2022, 11, 10)
fooddate3 = date(2022, 11, 6)
dateToday = date.today()
dateTomorrow = dateToday + timedelta1
dateYesterday = dateToday - timedelta1
dateMultDaysPassed = dateToday - timedelta2
dateWithinRange = dateToday + timedelta2
dateOutsideRange = dateToday + timedelta8

food1 = Food(name1, fooddate1, 3)
food2 = Food(name2, fooddate2, 3)
food3 = Food(name3, fooddate3, 2)
foodToday = Food(nameToday, dateToday, 2)
foodTomorrow = Food(nameTomorrow, dateTomorrow, 2)
foodYesterday = Food(nameYesterday, dateYesterday, 4)
foodPast = Food(namePast, dateMultDaysPassed, 3)
foodNearFuture = Food(nameNearFuture, dateWithinRange, 7)
foodFuture = Food(nameFuture, dateOutsideRange, 5)
