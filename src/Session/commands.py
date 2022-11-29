from src.Constants.commands_messages import *
from src.Constants.keys import *
from src.Session.profile import Profile
from src.FoodStorage.freezer import Freezer

class Commands:
    def __init__(self):
        self.profile = None

    def add_food(self):
        pass

    def remove_food(self):
        pass

    ''' Prompts user to create a new freezer. If no profile is active, suggests user to create or load one.
        If a freezer with this name exists, confirms with user if they want to override it.'''
    def create_freezer(self):
        if not self.profile:
            print(NO_LOADED_PROFILE_MESSAGE)
            print(SUGGESTED_ACTIONS_MESSAGE.format("'{}', '{}'".format(CREATE_PROFILE, LOAD)))
            return

        freezer_name = input(CREATE_FREEZER_NAME_MESSAGE)

        # Handle if a Freezer exists with this name
        if self.profile.getFoodStorage(FREEZER, freezer_name):
            while True:
                doOverride = input(CREATE_FREEZER_OVERRIDE_NAME.format(freezer_name))
                if doOverride == "n":
                    print(CANCEL_ACTION_MESSAGE.format(CREATE_FREEZER_ACTION.format(freezer_name)))
                    return
                elif doOverride == "y":
                    break
                else:
                    print(INVALID_RESPONSE_MESSAGE)
        
        self.profile.addFoodStorage(FREEZER, freezer_name)
        print(CREATE_FREEZER_SUCCESS_MESSAGE.format(freezer_name))

    def create_fridge(self):
        pass

    ''' Prompts user to create a new profile and name it. If there's already a 
        profile opened, we save it and then create a new profile with the given name. '''
    def create_profile(self):
        profile_name = input(CREATE_PROFILE_NAME_MESSAGE)

        if self.profile and self.profile.name != profile_name:
            self.profile.save()

        self.profile = Profile(profile_name)
        print(CREATE_PROFILE_SUCCESS_MESSAGE.format(profile_name))

    def help(self):
        pass

    def list_food_storages(self):
        pass

    def list_fridges(self):
        pass

    def list_freezers(self):
        pass

    def load(self, profile):
        pass
    
    def open(self, food_storage):
        pass

    def save(self):
        pass

    def delete(self, food_storage):
        pass
    
    def delete_profile(self):
        pass