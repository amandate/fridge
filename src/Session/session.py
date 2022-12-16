from os import listdir
from src.Constants.commands_messages import \
    SUGGESTED_ACTIONS_MESSAGE
from src.Constants.constants import \
    CREATE_PROFILE, \
    EMPTY_STRING, \
    EXIT, \
    JSON_EXTENSION, \
    PROFILES_PATH, \
    WITHIN_QUOTES
from src.Constants.session_messages import *
from src.Utils.utils import listSepByTab, twoPrintOutcomes

class Session:
    def __init__(self):
        self._profiles = self._getSavedProfiles()

    ''' Fetches currently saved profiles and returns their names in an array. '''
    def _getSavedProfiles(self):
        return [file.replace(JSON_EXTENSION, EMPTY_STRING) for file in sorted(listdir(PROFILES_PATH))]

    ''' Prints the welcome message the user sees when they first start our application.
        It will also print a list of profiles the user can load if there are any or
        prompt the user to create a new one. '''
    def _printWelcomeMessage(self):
        twoPrintOutcomes(self._profiles, [WELCOME_MESSAGE, LOAD_CREATE_PROFILE_MESSAGE], \
            [WELCOME_MESSAGE, NO_PROFILES_MESSAGE], CREATE_PROFILE)

    def _redirect(self, user_input):
        pass

    ''' This method starts a session. It will greet the user and then prompt the user
        to enter a command that will be redirected. '''
    def start(self):
        self._printWelcomeMessage()
        while True:
            user_input = input(ENTER_COMMAND_MESSAGE)
            self._redirect(user_input)
            if user_input == EXIT:
                break

    def end(self):
        pass 


