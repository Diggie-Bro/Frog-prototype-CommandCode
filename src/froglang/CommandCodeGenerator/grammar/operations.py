"""
operations.py
The Frog Programming Language Grammar: Operations

Development Leader: @RedoC
"""

import grammar.operation.equal as equal
import grammar.operation.boolean as boolean
import grammar.operation.assign as assign
import grammar.operation.dot as dot
import grammar.operation.range_ as range_
import grammar.operation.smallLarge as sl

# keyword
operationList = (
    "=",
    "and",
    "or",
    "not",
    ".",
    "==",
    "!=",
    "...",
    "..<",
    "<",
    ">",
    "<=",
    ">="
)

operationClassList = (
    assign.ASSIGN,
    boolean.AND,
    boolean.OR,
    boolean.NOT,
    dot.DOT,
    equal.EQUAL,
    equal.NOTEQUAL,
    range_.RANGE,  # ..., ..<
    sl.SMALL,
    sl.LARGE,
    sl.SMALLEQUAL,
    sl.LARGEEQUAL
)


def getOperation(word):
    """
    isOperation(word)
    check is 'word' in operationlist
    :param word:
    :return:
    """
    for operation in operationList:
        if operation in word:
            return operation
