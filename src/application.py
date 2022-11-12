from src.Food.food import Food
from src.FoodStorage.fridge import Fridge
from src.FoodStorage.freezer import Freezer

# Steps:
# File to handle commands
# File to create profile w/ profile_name, curr_date, map of names to food storages
#   - profile
#       - profile_name.json
#           - { "fridge1": [{"name": "apple", "expiration": "2022-11-08", "amt": 1}, ...]
#                   }
# File to reconstruct profiles


add_food = 'add food'
create_freezer = 'create freezer'
create_fridge = 'create fridge'
create_profile = 'create profile'
list_command = 'list'
list_food_storages = 'list food storages'
list_fridges = 'list fridges'
list_freezers = 'list freezers'
open = 'open'
save = "save"

def _listCommands():
    print(create_freezer, create_fridge, list_command, sep = "\n")

def _displayWelcomeScreen():
    return input("Welcome! Please enter your command or type 'list' to list commands: ")

if '__name__' == '__main__':
    action = _displayWelcomeScreen()
    while True:
        if action == create_freezer:
            pass
        elif action == create_fridge:
            pass
        elif action == list_command:
            pass
        else:
            print("I'm sorry, I don't recognize that command. Type 'list' to see a list of available commands.")
        action = input()
