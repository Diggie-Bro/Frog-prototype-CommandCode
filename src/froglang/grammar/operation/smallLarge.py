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

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of large expr
        :return:
        """
        bytecode = "LARGE ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


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

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of large or equal expr
        :return:
        """
        bytecode = "NOTEQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


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

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of small expr
        :return:
        """
        bytecode = "SMALL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


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

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of small or equal expr
        :return:
        """
        bytecode = "SMALLEQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    large_ = LARGE("foo", "32")
    print(large_.getBytecode())

    largeequal_ = LARGEEQUAL("32 + 5", "64 + 9")
    print(largeequal_.getBytecode())

    small_ = LARGE("foo", "32")
    print(small_.getBytecode())

    smallequal_ = LARGEEQUAL("32 + 5", "64 + 9")
    print(smallequal_.getBytecode())
