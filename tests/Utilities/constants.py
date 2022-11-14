from src.Food.food import Food
from datetime import date, timedelta

timedelta1 = timedelta(days=1)
timedelta2 = timedelta(days=2)
timedelta8 = timedelta(days=8)

fooddate1 = date(2022, 11, 8)
fooddate2 = date(2022, 11, 10)
fooddate3 = date(2022, 11, 6)
dateToday = date.today()
dateTomorrow = dateToday + timedelta1
dateYesterday = dateToday - timedelta1
dateMultDaysPassed = dateToday - timedelta2
dateWithinRange = dateToday + timedelta2
dateOutsideRange = dateToday + timedelta8

food1 = Food("apple", fooddate1, 3)
food2 = Food("pear", fooddate2, 3)
food3 = Food("banana", fooddate3, 2)
foodToday = Food("grape", dateToday, 2)
foodTomorrow = Food("curry", dateTomorrow, 2)
foodYesterday = Food("grape", dateYesterday, 4)
foodPast = Food("noodles", dateMultDaysPassed, 3)
foodNearFuture = Food("lettuce", dateWithinRange, 7)
foodFuture = Food("meat", dateOutsideRange, 5)
