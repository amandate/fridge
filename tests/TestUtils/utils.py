from src.Constants.constants import FOOD_STORAGE
from src.Session.profile import Profile

def isEmptyInventory(foodStorage):
    return foodStorage.list() == []
