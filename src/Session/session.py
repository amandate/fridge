from os import listdir
from src.Constants.commands_messages import INVALID_RESPONSE_MESSAGE    
from src.Constants.constants import \
    ADD_FOOD, \
    CREATE_FOOD_STORAGE, \
    CREATE_FREEZER, \
    CREATE_FRIDGE, \
    CREATE_PROFILE, \
    DELETE_FOOD_STORAGE, \
    DELETE_FREEZER, \
    DELETE_FRIDGE, \
    DELETE_PROFILE, \
    EMPTY_STRING, \
    EXIT, \
    HELP, \
    LIST_FOOD_STORAGES, \
    LIST_FREEZERS, \
    LIST_FRIDGES, \
    LOAD, \
    JSON_EXTENSION, \
    OPEN_FOOD_STORAGE, \
    OPEN_FREEZER, \
    OPEN_FRIDGE, \
    PROFILES_PATH, \
    REMOVE_FOOD, \
    SAVE, \
    SPACE
from src.Constants.session_messages import *
from src.Session.commands import Commands
from src.Utils.utils import twoPrintOutcomes

class Session:
    def __init__(self):
        self._profiles = self._getSavedProfiles()
        self._commands = Commands()

    ''' Fetches currently saved profiles and returns their names in an array. '''
    def _getSavedProfiles(self):
        return [file.replace(JSON_EXTENSION, EMPTY_STRING) for file in sorted(listdir(PROFILES_PATH))]

    ''' Redirects user_input to the correct command method. '''
    def _redirect(self, user_input):
        if user_input == ADD_FOOD:
            self._commands.add_food()
        elif user_input == CREATE_FOOD_STORAGE or \
            user_input == CREATE_FREEZER or \
            user_input == CREATE_FRIDGE:
            self._commands.create_foodStorage(SPACE.join(user_input.split()[1:]))
        elif user_input == CREATE_PROFILE:
            self._commands.create_profile()
        elif user_input == DELETE_FOOD_STORAGE or \
            user_input == DELETE_FREEZER or \
            user_input == DELETE_FRIDGE:
            self._commands.delete(SPACE.join(user_input.split()[1:]))
        elif user_input == DELETE_PROFILE:
            self._commands.delete_profile()
        elif user_input == EXIT:
            return 0
        elif user_input == HELP:
            self._commands.help()
        elif user_input == LIST_FOOD_STORAGES or \
            user_input == LIST_FREEZERS or \
            user_input == LIST_FRIDGES:
            user_input = user_input[:-1]
            self._commands.list_food_storages(SPACE.join(user_input.split()[1:]))
        elif user_input.startswith(LOAD):
            self._commands.load(SPACE.join(user_input.split()[1:]))
        elif user_input == OPEN_FOOD_STORAGE or \
            user_input == OPEN_FREEZER or \
            user_input == OPEN_FRIDGE:
            self._commands.open(SPACE.join(user_input.split()[1:]))
        elif user_input == REMOVE_FOOD:
            self._commands.remove_food()
        elif user_input == SAVE:
            self._commands.save()
        else:
            print(INVALID_RESPONSE_MESSAGE)
        return 1

    ''' This method starts a session. It will greet the user and then prompt the user
        to enter a command that will be redirected. If the redirect was unsuccessful or
        the user requests 'exit', we will break and exit the program. '''
    def start(self):
        twoPrintOutcomes(self._profiles, [WELCOME_MESSAGE, LOAD_CREATE_PROFILE_MESSAGE], \
            [WELCOME_MESSAGE, NO_PROFILES_MESSAGE], [CREATE_PROFILE])
        while True:
            user_input = input(ENTER_COMMAND_MESSAGE).strip()
            success = self._redirect(user_input)
            if not success:
                break