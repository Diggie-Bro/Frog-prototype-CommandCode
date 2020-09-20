"""
equal.py
The Frog Programming Language Operation: equal & not equal

Black lives matter. We support all resistance of racism.

Development Leader: @RedoC
"""


class EQUAL:
    """
    EQUAL is the operation class
    >> example
    foo == boo
    foo == 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcodeBegin(self)
        get commandcode of equal
        :return:
        """
        commandcode = "EQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


class NOTEQUAL:
    """
    NOTEQUAL is the operation class
    >> example
    foo != boo
    foo != 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of notequal
        :return:
        """
        commandcode = "NOTEQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    equal_ = EQUAL("foo", 36)
    print(equal_.getCommandcode())
    notequal_ = NOTEQUAL("foo", "boo")
    print(notequal_.getCommandcode())

