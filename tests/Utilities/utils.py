''' Adds multiple foods into our food storage. '''
def addMultipleFoods(foodStorage, foods):
    foodStorage.addFoods(foods)

def isEmptyInventory(foodStorage):
    return foodStorage.list() == []