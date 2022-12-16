from src.Constants.commands_messages import SUGGESTED_ACTIONS_MESSAGE
from src.Constants.constants import \
    COMMA, \
    SPACE, \
    TAB, \
    WITHIN_QUOTES

''' Takes in an array and returns a string that's a listing of each 
    object surrounded by quotes and separated by commas. '''
def listInQuotes(array):
    return (COMMA+SPACE).join([WITHIN_QUOTES.format(x) for x in array])

''' Takes in an array and returns a string that's a listing of each 
    object separated by a tab. '''
def listSepByTab(array):
    return TAB.join(array)

''' Takes in an array and prints 2 outcomes and corresponding messages depending on 
    if the array is empty or not. '''
def twoPrintOutcomes(array, posOutcome, negOutcome, suggestedActions):
    if array:
        print(SPACE.join(posOutcome))
        print(listSepByTab(array))
    else:
        print(SPACE.join(negOutcome))
        print(SUGGESTED_ACTIONS_MESSAGE.format(listInQuotes(suggestedActions)))