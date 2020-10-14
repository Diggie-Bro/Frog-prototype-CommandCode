"""
smallLarge.py
The Frog Programming Language Operation: large, large or equal, small, small or equal

Development Leader: @RedoC
"""


class LARGE:
    """
    LARGE is the operation class
    >> example
    foo > boo
    foo > 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcodeBegin(self)
        get commandcode of large expr
        :return:
        """
        commandcode = "LARGE ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


class LARGEEQUAL:
    """
    LARGEEQUAL is the operation class
    >> example
    foo >= boo
    foo >= 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of large or equal expr
        :return:
        """
        commandcode = "NOTEQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


class SMALL:
    """
    SMALL is the operation class
    >> example
    foo < boo
    foo < 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcodeBegin(self)
        get commandcode of small expr
        :return:
        """
        commandcode = "SMALL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


class SMALLEQUAL:
    """
    SMALLEQUAL is the operation class
    >> example
    foo <= boo
    foo <= 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of small or equal expr
        :return:
        """
        commandcode = "SMALLEQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    large_ = LARGE("foo", "32")
    print(large_.getCommandcode())

    largeequal_ = LARGEEQUAL("32 + 5", "64 + 9")
    print(largeequal_.getCommandcode())

    small_ = LARGE("foo", "32")
    print(small_.getCommandcode())

    smallequal_ = LARGEEQUAL("32 + 5", "64 + 9")
    print(smallequal_.getCommandcode())
