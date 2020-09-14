"""
const_.py
The Frog Programming Language Grammar: const

Development Leader: @RedoC
"""


class FrogCONST:
    """
    FrogCONST is the grammar class
    """

    def __init__(self, name: str, init):
        self.name = name
        self.init = init

    def getBytecode(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin const
        :return:
        """
        bytecode = "CONST ({name})({init})".format(name=self.name, init=self.init)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    const_ = FrogCONST("foo", 36)
    print(const_.getBytecode())
