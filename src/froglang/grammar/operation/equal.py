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

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of equal
        :return:
        """
        bytecode = "EQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


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

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of notequal
        :return:
        """
        bytecode = "NOTEQUAL ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    equal_ = EQUAL("foo", 36)
    print(equal_.getBytecode())
    notequal_ = NOTEQUAL("foo", "boo")
    print(notequal_.getBytecode())

