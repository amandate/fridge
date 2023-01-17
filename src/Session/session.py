from os import listdir    
from src.Constants.constants import \
    CREATE_PROFILE, \
    EMPTY_STRING, \
    EXIT, \
    JSON_EXTENSION, \
    PROFILES_PATH
from src.Constants.session_messages import *
from src.Utils.utils import twoPrintOutcomes

class Session:
    def __init__(self):
        self._profiles = self._getSavedProfiles()

    ''' Fetches currently saved profiles and returns their names in an array. '''
    def _getSavedProfiles(self):
        return [file.replace(JSON_EXTENSION, EMPTY_STRING) for file in sorted(listdir(PROFILES_PATH))]

    def _redirect(self, user_input):
        pass

    ''' This method starts a session. It will greet the user and then prompt the user
        to enter a command that will be redirected. '''
    def start(self):
        twoPrintOutcomes(self._profiles, [WELCOME_MESSAGE, LOAD_CREATE_PROFILE_MESSAGE], \
            [WELCOME_MESSAGE, NO_PROFILES_MESSAGE], [CREATE_PROFILE])
        while True:
            user_input = input(ENTER_COMMAND_MESSAGE)
            self._redirect(user_input)
            if user_input == EXIT:
                break

    def end(self):
        pass 


