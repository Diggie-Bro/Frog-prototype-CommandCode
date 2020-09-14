"""
except_.py
The Frog Programming Language Grammar: except

Development Leader: @RedoC
"""


class FrogEXCEPT:
    """
    FrogEXCEPT is the grammar class
    """

    def __init__(self, error: str):
        self.error = error

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin except
        :return:
        """
        bytecode = "(BEGINEXCEPT ({})".format(self.error)    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end except
        :return:
        """
        bytecode = "ENDEXCEPT)"    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    except_ = FrogEXCEPT("StackOverflow")
    print(except_.getBytecodeBegin())
    print(except_.getBytecodeEND())
