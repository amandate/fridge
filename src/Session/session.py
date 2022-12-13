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
from src.Utils.utils import listSepByTab

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
        if len(self._profiles):
            print(WELCOME_MESSAGE, LOAD_CREATE_PROFILE_MESSAGE)
            print(listSepByTab(self._profiles))
        else:
            print(WELCOME_MESSAGE, NO_PROFILES_MESSAGE)
            print(SUGGESTED_ACTIONS_MESSAGE.format(WITHIN_QUOTES.format(CREATE_PROFILE)))

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


