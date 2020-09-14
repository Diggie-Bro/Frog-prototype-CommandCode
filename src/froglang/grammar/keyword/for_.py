"""
for_.py
The Frog Programming Language Grammar: for

Development Leader: @RedoC
"""


class FrogFOR:
    """
    FrogFOR is the grammar class
    """

    def __init__(self, statement: str):
        self.statement = statement

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin for
        :return:
        """
        bytecode = "(BEGINFOR ({})".format(self.statement)    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end for
        :return:
        """
        bytecode = "ENDFOR)".format(self.statement)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    for_ = FrogFOR("foo > boo")
    print(for_.getBytecodeBegin())
    print(for_.getBytecodeEND())

