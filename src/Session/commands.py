from src.Constants.commands_messages import *
from src.Constants.constants import *
from src.Session.profile import Profile
from src.Utils.utils import listInQuotes

class Commands:
    def __init__(self):
        self.profile = None

    def add_food(self):
        pass

    def remove_food(self):
        pass

    ''' Prompts user to create a new food storage. If no profile is active, suggests user to create or load one.
        If a food storage with this name exists, confirms with user if they want to override it.'''
    def create_foodStorage(self, foodStorage_type):
        if not self.profile:
            print(NO_LOADED_PROFILE_MESSAGE, \
                SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes([CREATE_PROFILE, LOAD])))
            return

        foodStorage_name = input(CREATE_FOOD_STORAGE_NAME_MESSAGE.format(foodStorage_type))

        # Handle if a food storage exists with this name
        if self.profile.getFoodStorage(foodStorage_type, foodStorage_name):
            while True:
                override_request = EXISTING_NAME_MESSAGE.format(foodStorage_type, foodStorage_name) + \
                                    OVERRIDE_REQUEST_MESSAGE.format(foodStorage_type)
                doOverride = input(override_request)
                if doOverride == NO:
                    print(CANCEL_ACTION_MESSAGE.format(CREATE_FOOD_STORAGE_ACTION.format(foodStorage_type, foodStorage_name)))
                    return
                elif doOverride == YES:
                    break
                else:
                    print(INVALID_RESPONSE_MESSAGE)
        
        self.profile.addFoodStorage(foodStorage_type, foodStorage_name)
        print(CREATE_FOOD_STORAGE_SUCCESS_MESSAGE.format(foodStorage_type, foodStorage_name))

    ''' Prompts user to create a new profile and name it. If there's already a 
        profile opened, we save it and then create a new profile with the given name. '''
    def create_profile(self):
        profile_name = input(CREATE_PROFILE_NAME_MESSAGE)

        if self.profile and self.profile.name != profile_name:
            self.profile.save()

        self.profile = Profile(profile_name)
        print(CREATE_PROFILE_SUCCESS_MESSAGE.format(profile_name))

    ''' Displays available commands when prompted by user. '''
    def help(self):
        print(ADD_FOOD, \
             CREATE_FREEZER, \
             CREATE_FRIDGE, \
             CREATE_PROFILE, \
             DELETE, \
             DELETE_PROFILE, \
             LIST_FOOD_STORAGES, \
             LIST_FREEZERS, \
             LIST_FRIDGES, \
             LOAD, \
             OPEN, \
             REMOVE_FOOD, \
             SAVE, \
             sep = NEW_LINE)

    def list_food_storages(self):
        pass

    def list_fridges(self):
        pass

    def list_freezers(self):
        pass

    def load(self, profile):
        pass
  
    ''' Prompts user input to open a food storage. If a food storage with that name does not exist, 
        prompts user to create a new one. '''
    def open(self, foodStorage_type):
        foodStorage_list = self.profile.listFoodStorages(foodStorage_type)
        print(OPEN_FOOD_STORAGE_MESSAGE.format(foodStorage_type))
        
        foodStorage_name = input(OPEN_FOOD_STORAGE_NAME.format(foodStorage_type))

        # Handle if a food storage does not exist with this name.
        if not self.profile.open(foodStorage_type, foodStorage_name):
            while True:
                newStorage_request = NEW_FOOD_STORAGE_REQUEST_MESSAGE.format(foodStorage_type) 
                doNewStorage = input(newStorage_request)
                if doNewStorage == YES:
                    self.create_foodStorage(foodStorage_type)
                    return
                elif doNewStorage == NO:
                    print(CANCEL_ACTION_MESSAGE.format(OPEN_FOOD_STORAGE_ACTION.format(foodStorage_type)))
                    return 
                else:
                    print(INVALID_RESPONSE_MESSAGE)
        
        print(OPEN_FOOD_STORAGE_SUCCESS_MESSAGE.format(foodStorage_name))
                   
    def save(self):
        pass

    def delete(self, food_storage):
        pass
    
    def delete_profile(self):
        pass