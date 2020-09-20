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

    def getCommandcode(self):
        """
        getCommandcodeBegin(self)
        get commandcode of and
        :return:
        """
        commandcode = "AND ({s1})({s2})".format(s1=self.state1, s2=self.state2)    # commandcode
        return commandcode


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

    def getCommandcode(self):
        """
        getCommandcodeBegin(self)
        get commandcode of or
        :return:
        """
        commandcode = "OR ({s1})({s2})".format(s1=self.state1, s2=self.state2)    # commandcode
        return commandcode


class NOT:
    """
    NOT is the operation class
    >> example
    not boo
    not 14 < 2 * 7
    """

    def __init__(self, state: str):
        self.state = state

    def getCommandcode(self):
        """
        getCommandcodeBegin(self)
        get commandcode of not
        :return:
        """
        commandcode = "NOT ({})".format(self.state)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    and_ = AND("foo", "36 > 50")
    print(and_.getCommandcode())
    or_ = OR("90 == 90", "50 < 100")
    print(or_.getCommandcode())
    not_ = NOT(or_.getCommandcode())
    print(not_.getCommandcode())

