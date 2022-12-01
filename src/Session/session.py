from os import listdir
from src.Constants.keys import \
    EMPTY_STRING, \
    JSON_EXTENSION, \
    PROFILES_PATH, \
    TAB_STRING
from src.Constants.session_messages import *

class Session:
    def __init__(self):
        self.profiles = self._getSavedProfiles()

    def _getSavedProfiles(self):
        return [file.replace(JSON_EXTENSION, EMPTY_STRING) for file in sorted(listdir(PROFILES_PATH))]

    def _printSavedProfiles(self):
        print(TAB_STRING.join(self.profiles))

    def redirect(self, user_input):
        pass

    def start(self):
        print(WELCOME_MESSAGE)
        self._printSavedProfiles()
        while True:
            user_input = input()
            self.redirect(user_input)

    def end(self):
        pass 


