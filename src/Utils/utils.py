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