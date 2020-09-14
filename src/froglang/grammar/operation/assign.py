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

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of assign
        :return:
        """
        bytecode = "ASSIGN ({name})({operand})".format(name=self.name, operand=(
            self.val if self.val is not None else self.operand))    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    assign_ = ASSIGN("foo", 36)
    print(assign_.getBytecode())
