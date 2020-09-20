"""
range.py
The Frog Programming Language Operation: range

Development Leader: @RedoC
"""


class RANGE:
    """
    RANGE is the operation class
    >> example
    1...5 => 1, 2, 3, 4, 5
    1..<5 => 1, 2, 3, 4
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcodeDotDotDot(self):  # ...
        """
        getCommandcodeDotDotDot(self)
        get commandcode of range (...)
        :return:
        """
        commandcode = "RANGECLOSED ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))  # commandcode
        return commandcode

    def getCommandcodeDotDotBig(self):  # ..<
        """
        getCommandcodeDotDotBig(self)
        get commandcode of range (..<)
        :return:
        """
        commandcode = "RANGEOPENED ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))  # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    range_ = RANGE("foo", 36)
    print(range_.getCommandcodeDotDotDot())
    print(range_.getCommandcodeDotDotBig())
