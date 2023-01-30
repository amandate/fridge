from src.Constants.commands_messages import *
from src.Constants.constants import *
from src.Session.profile import Profile
from src.Utils.utils import listInQuotes, twoPrintOutcomes

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
            DELETE_FOOD_STORAGE, \
            DELETE_FREEZER, \
            DELETE_FRIDGE, \
            DELETE_PROFILE, \
            LIST_FOOD_STORAGES, \
            LIST_FREEZERS, \
            LIST_FRIDGES, \
            LOAD, \
            OPEN_FOOD_STORAGE, \
            OPEN_FREEZER, \
            OPEN_FRIDGE, \
            REMOVE_FOOD, \
            SAVE, \
            sep = NEW_LINE)

    ''' Allows user to list available food storages. '''
    def list_food_storages(self, foodStorage_type):
        # Checks if a profile is loaded -> if not, prompts to load or create one
        if not self.profile:
            print(NO_LOADED_PROFILE_MESSAGE, \
                SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes([CREATE_PROFILE, LOAD])))
            return
        
        foodStorage_list = self.profile.listFoodStorages(foodStorage_type)

        twoPrintOutcomes(foodStorage_list, [LIST_FOOD_STORAGES_ACTION.format(foodStorage_type)], \
            [NO_FOOD_STORAGE_MESSAGE.format(foodStorage_type)], [CREATE_FOOD_STORAGE, CREATE_FREEZER, CREATE_FRIDGE]) 

    def load(self, profile):
        pass 
  
    ''' Prompts user input to open a food storage. Also lists available food storages user can choose from. 
        If a food storage is not available or a food storage with that name does not exist, prompts user to create a new one. '''
    def open(self, foodStorage_type):
        # Checks if a profile is loaded -> if not, prompts to load or create one
        if not self.profile:
            print(NO_LOADED_PROFILE_MESSAGE, \
                SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes([CREATE_PROFILE, LOAD])))
            return

        # Compiles list of food storages available
        foodStorage_list = self.profile.listFoodStorages(foodStorage_type)

        # If there are food storages available, prints open message and lists available food storages.
        # If there are no food storages, prompts user to create one.
        isPosOutcome = twoPrintOutcomes(foodStorage_list, [OPEN_FOOD_STORAGE_MESSAGE.format(foodStorage_type)], \
            [NO_FOOD_STORAGE_MESSAGE.format(foodStorage_type)], [CREATE_FOOD_STORAGE, CREATE_FREEZER, CREATE_FRIDGE]) 
        if not isPosOutcome:
            return
            
        # Handles user input for food storage name 
        foodStorage_name = input(OPEN_FOOD_STORAGE_NAME.format(foodStorage_type))

        # Handle if a food storage does not exist with this name.
        if not self.profile.open(foodStorage_type, foodStorage_name):
            while True:
                newStorage_request = NON_EXISTING_NAME_MESSAGE.format(foodStorage_type, foodStorage_name) + \
                    CREATE_NEW_OBJECT_REQUEST_MESSAGE
                doNewStorage = input(newStorage_request)
                if doNewStorage == YES:
                    return self.create_foodStorage(foodStorage_type)
                elif doNewStorage == NO:
                    print(CANCEL_ACTION_MESSAGE.format(OPEN_FOOD_STORAGE_ACTION.format(foodStorage_type)))
                    return 
                else:
                    print(INVALID_RESPONSE_MESSAGE)
        
        # If food storage exists with this name, prints open success message. 
        print(OPEN_FOOD_STORAGE_SUCCESS_MESSAGE.format(foodStorage_type, foodStorage_name))
                   
    def save(self):
        pass

    def delete(self, food_storage):
        pass
    
    def delete_profile(self):
        pass