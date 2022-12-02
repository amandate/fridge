from os import listdir
from src.Constants.constants import \
    EMPTY_STRING, \
    EXIT, \
    JSON_EXTENSION, \
    PROFILES_PATH, \
    TAB_STRING
from src.Constants.session_messages import *

class Session:
    def __init__(self):
        self._profiles = self._getSavedProfiles()

    def _getSavedProfiles(self):
        return [file.replace(JSON_EXTENSION, EMPTY_STRING) for file in sorted(listdir(PROFILES_PATH))]

    def _printSavedProfiles(self):
        print(TAB_STRING.join(self._profiles))

    def _redirect(self, user_input):
        pass

    def start(self):
        print(WELCOME_MESSAGE, LOAD_CREATE_PROFILE_MESSAGE)
        self._printSavedProfiles()
        while True:
            user_input = input(ENTER_COMMAND_MESSAGE)
            self._redirect(user_input)
            if user_input == EXIT:
                break

    def end(self):
        pass 


