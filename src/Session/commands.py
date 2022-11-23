from src.Constants.commands_messages import *
from src.Session.profile import Profile

class Commands:
    def __init__(self):
        self.profile = None

    def add_food(self):
        pass

    def remove_food(self):
        pass

    def create_freezer(self):
        pass

    def create_fridge(self):
        pass

    ''' Prompts user to create a new profile and name it. If there's already a 
        profile opened, we save it and then create a new profile with the given name. '''
    def create_profile(self):
        profile_name = input(CREATE_PROFILE_NAME)

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