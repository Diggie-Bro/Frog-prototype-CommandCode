"""
if_.py
The Frog Programming Language Grammar: if

Development Leader: @RedoC
"""


class FrogIF:
    """
    FrogIF is the grammar class
    """

    def __init__(self, statement: str):
        self.statement = statement

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin if
        :return:
        """
        bytecode = "(BEGINIF ({})".format(self.statement)    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end if
        :return:
        """
        bytecode = "ENDIF)".format(self.statement)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    if_ = FrogIF("foo > boo")
    print(if_.getBytecodeBegin())
    print(if_.getBytecodeEND())

