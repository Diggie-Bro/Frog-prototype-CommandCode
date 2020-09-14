"""
boolean.py
The Frog Programming Language Operation: and, or, not

Development Leader: @RedoC
"""


class AND:
    """
    AND is the operation class
    >> example
    foo and boo
    13 > 12 and 19 < 5
    """

    def __init__(self, state1: str, state2: str):
        self.state1 = state1
        self.state2 = state2

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of and
        :return:
        """
        bytecode = "AND ({s1})({s2})".format(s1=self.state1, s2=self.state2)    # bytecode
        return bytecode


class OR:
    """
    OR is the operation class
    >> example
    foo or boo
    13 > 12 or 19 < 5
    """

    def __init__(self, state1: str, state2: str):
        self.state1 = state1
        self.state2 = state2

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of or
        :return:
        """
        bytecode = "OR ({s1})({s2})".format(s1=self.state1, s2=self.state2)    # bytecode
        return bytecode


class NOT:
    """
    NOT is the operation class
    >> example
    not boo
    not 14 < 2 * 7
    """

    def __init__(self, state: str):
        self.state = state

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of not
        :return:
        """
        bytecode = "NOT ({})".format(self.state)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    and_ = AND("foo", "36 > 50")
    print(and_.getBytecode())
    or_ = OR("90 == 90", "50 < 100")
    print(or_.getBytecode())
    not_ = NOT(or_.getBytecode())
    print(not_.getBytecode())

