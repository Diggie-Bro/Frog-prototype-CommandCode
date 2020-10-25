"""
parens.py
The Frog Programming Language Util Tool

Development Leader: @RedoC
"""

def parseParens(code: str):
    """
    parseParens(code: str)
    parse paren structure

    :param code: str
    """
    accumulator = []
    parensList = []
    isTopLevel = True
    for ind, char in enumerate(list(code)):
        if char == '(':
            isTopLevel = True
            accumulator.append(ind)
        elif char == ')':
            if isTopLevel == True:
                lastind = accumulator.pop(len(accumulator) - 1)
                parensList.append(code[lastind + 1: ind])
                isTopLevel = False
    return parensList


# unit test
if __name__ == '__main__':
    print(parseParens('BEGINELIF (AND (yes=="no")(yes=="no"))'))

