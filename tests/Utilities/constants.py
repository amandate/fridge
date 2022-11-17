from src.Food.food import Food
from datetime import date, timedelta

timedelta1 = timedelta(days=1)
timedelta2 = timedelta(days=2)
timedelta8 = timedelta(days=8)

name1 = "apple"
name2 = "pear"

fooddate1 = date(2022, 11, 8)
fooddate2 = date(2022, 11, 10)
fooddate3 = date(2022, 11, 6)
dateToday = date.today()
dateTomorrow = dateToday + timedelta1
dateYesterday = dateToday - timedelta1
dateMultDaysPassed = dateToday - timedelta2
dateWithinRange = dateToday + timedelta2
dateOutsideRange = dateToday + timedelta8

food1 = Food(name1, fooddate1.isoformat(), 3)
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
