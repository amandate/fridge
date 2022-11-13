from src.Food.food import Food
from datetime import date, timedelta

fooddate1 = date(2022, 11, 8)
fooddate2 = date(2022, 11, 10)
fooddate3 = date(2022, 11, 6)
dateToday = date.today()
dateTomorrow = dateToday + timedelta(days=1)
dateOutsideRange = dateToday + timedelta(days=8)

food1 = Food("apple", fooddate1, 3)
food2 = Food("pear", fooddate2, 3)
food3 = Food("banana", fooddate3, 2)
foodToday = Food("grape", dateToday, 2)
foodTomorrow = Food("curry", dateTomorrow, 2)
foodFuture = Food("meat", dateOutsideRange, 5)
