from datetime import date
from src.Constants.constants import *
from src.FoodStorage.foodStorage import FoodStorage
from src.FoodStorage.freezer import Freezer
from src.FoodStorage.fridge import Fridge

import json 

class Profile:
    def __init__(self, name):
        self.name = name
        self.current_date = date.today()
        self._foodStorages = {}
        self._opened_foodStorage = None

    ''' Adds a new FoodStorage object of foodStorage_type with the given name and 
        sets self._opened_foodStorage to it. '''
    def addFoodStorage(self, foodStorage_type, name):
        if foodStorage_type not in self._foodStorages:
            self._foodStorages[foodStorage_type] = {}
        
        newFoodStorage = FoodStorage()
        if foodStorage_type == FREEZER:
            newFoodStorage = Freezer()
        elif foodStorage_type == FRIDGE:
            newFoodStorage = Fridge()

        self._foodStorages[foodStorage_type][name] = newFoodStorage
        self.open(foodStorage_type, name) 

    ''' Gets the FoodStorage object of foodStorage_type with the given name. 
        Returns None if it does not exist. '''
    def getFoodStorage(self, foodStorage_type, name):
        if foodStorage_type not in self._foodStorages or \
            name not in self._foodStorages[foodStorage_type]:
            return None
        return self._foodStorages[foodStorage_type][name]

    ''' Retrieves FoodStorage object with getFoodStorage method and sets it 
        to open if it exists, otherwise return 0. '''
    def open(self, foodStorage_type, name):
        retrievedFoodStorage = self.getFoodStorage(foodStorage_type, name)
        if retrievedFoodStorage is not None:
            self._opened_foodStorage = retrievedFoodStorage
            self._opened_foodStorage.open()
            return 1
        return 0

    ''' Lists names of added items in the FoodStorages. If food storage 
        type does not exist, returns a blank list. '''
    def listFoodStorages(self, foodStorage_type): 
        if foodStorage_type == FOOD_STORAGE:
            allNames = []
            for type in self._foodStorages.keys():
                allNames += list(self._foodStorages[type].keys())
            return allNames
        elif foodStorage_type not in self._foodStorages:
            return []
        return list(self._foodStorages[foodStorage_type].keys())
    
    def load(self, name):
        pass

    def save(self):
        user_profile = {
            PROFILE_NAME : self.name, 
            FOOD_STORAGES : {
                
            }
        }  
        # creates array by food storage type
        for type in self._foodStorages:
            user_profile[FOOD_STORAGES][type] = []

            for food_storage_name in self._foodStorages[type]:
                foodStorage_dictionary = self._foodStorages[type][food_storage_name].asDictionary()
                foodStorage_dictionary['name'] = food_storage_name
                user_profile[FOOD_STORAGES][type].append(foodStorage_dictionary)

        json_profile = json.dumps(user_profile, indent=4)
       
        with open(PROFILES_PATH + SLASH + self.name + JSON_EXTENSION, "w") as outfile:
            outfile.write(json_profile)
        