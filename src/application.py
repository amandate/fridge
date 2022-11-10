from src.Food.food import Food
from src.FoodStorage.fridge import Fridge
from src.FoodStorage.freezer import Freezer

create_freezer = 'create freezer'
create_fridge = 'create fridge'
list_command = 'list'
list_fridges = 'list fridges'
list_freezers = 'list freezers'
open_fridge = 'open '

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
