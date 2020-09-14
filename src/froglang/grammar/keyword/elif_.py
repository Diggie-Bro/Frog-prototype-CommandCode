"""
elif_.py
The Frog Programming Language Grammar: elif

Development Leader: @RedoC
"""


class FrogELIF:
    """
    FrogELIF is the grammar class
    """

    def __init__(self, statement: str):
        self.statement = statement

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin elif
        :return:
        """
        bytecode = "(BEGINELIF ({})".format(self.statement)    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end elif
        :return:
        """
        bytecode = "ENDELIF)".format(self.statement)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    elif_ = FrogELIF("foo > boo")
    print(elif_.getBytecodeBegin())
    print(elif_.getBytecodeEND())

