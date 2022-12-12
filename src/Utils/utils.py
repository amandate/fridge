from src.Constants.constants import \
    COMMA, \
    SPACE, \
    TAB, \
    WITHIN_QUOTES

def listInQuotes(array):
    return (COMMA+SPACE).join([WITHIN_QUOTES.format(x) for x in array])

def listSepByTab(array):
    return TAB.join(array)