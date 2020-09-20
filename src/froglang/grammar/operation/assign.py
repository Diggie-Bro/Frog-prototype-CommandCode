"""
assign.py
The Frog Programming Language Operation: assign

Development Leader: @RedoC
"""


class ASSIGN:
    """
    ASSIGN is the operation class
    >> example
    foo = boo
    foo = 12
    """

    def __init__(self, name: str, val=None, operand=None):
        self.name = name
        self.val = val
        self.operand = operand

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of assign
        :return:
        """
        commandcode = "ASSIGN ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    assign_ = ASSIGN("foo", 36)
    print(assign_.getCommandcode())
