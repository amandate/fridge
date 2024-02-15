from datetime import date
from src.Constants.constants import *
from src.Food.food import Food
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
        # print(newFoodStorage)
        self.open(foodStorage_type, name) 

    ''' Gets the FoodStorage object of foodStorage_type with the given name. 
        Returns None if it does not exist. '''
    def getFoodStorage(self, foodStorage_type, name):
        if foodStorage_type not in self._foodStorages or \
            name not in self._foodStorages[foodStorage_type]:
            return None
        return self._foodStorages[foodStorage_type][name] # <src.FoodStorage.fridge.Fridge object at 0x102be2380>

    ''' Retrieves FoodStorage object with getFoodStorage method and sets it 
        to open if it exists, otherwise return 0. '''
    def open(self, foodStorage_type, name):
        retrievedFoodStorage = self.getFoodStorage(foodStorage_type, name)
        if retrievedFoodStorage is not None:
            self._opened_foodStorage = retrievedFoodStorage
            self._opened_foodStorage.open()
            return 1
        return 0
    
    ''' Checks if a food storage is opened. '''
    def getOpenFoodStorage(self):
        return self._opened_foodStorage 

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
        # print(list(self._foodStorages[foodStorage_type].keys())) # ['kitchen', 'garage']
        return list(self._foodStorages[foodStorage_type].keys())
    
    ''' Adds array of foods to the opened food storage that the user is in.  
        Can add multiple food items. '''
    def addFoods(self, foods):
        if self._opened_foodStorage:
            self._opened_foodStorage.addFoods(foods)
            return 1
        return 0

    ''' Checks if self.name of food items are the same. '''
    def __eq__(self, other):
        return self.name == other.name and self._foodStorages == other._foodStorages 

    ''' Checks if self.name of food items are not the same. '''
    def __ne__(self, other):
        return self.name == other.name or self._foodStorages != other._foodStorages

    ''' Takes information provided by user and creates a json with the profile information saved to it. '''
    def save(self):
        user_profile = {
            NAME : self.name, 
            FOOD_STORAGES : {}
        }  
        # Creates array by food storage type.
        for type in self._foodStorages:
            user_profile[FOOD_STORAGES][type] = []
            # Accesses self._foodStorages to pull information of food storages and food objects and 
            # appends them to the empty array.
            for food_storage_name in self._foodStorages[type]:
                foodStorage_dictionary = self._foodStorages[type][food_storage_name].asDictionary()
                foodStorage_dictionary[NAME] = food_storage_name
                user_profile[FOOD_STORAGES][type].append(foodStorage_dictionary)

        # Creates the .json file for user profile.
        json_profile = json.dumps(user_profile, indent=4)     
        with open(PROFILES_PATH + SLASH + self.name + JSON_EXTENSION, "w") as outfile:
            outfile.write(json_profile)
        