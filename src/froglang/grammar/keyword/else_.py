"""
else_.py
The Frog Programming Language Grammar: else

Development Leader: @RedoC
"""


class FrogELSE:
    """
    FrogELSE is the grammar class
    """

    def __init__(self):
        pass

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin else
        :return:
        """
        bytecode = "(BEGINELSE"    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end else
        :return:
        """
        bytecode = "ENDELSE)"    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    else_ = FrogELSE()
    print(else_.getBytecodeBegin())
    print(else_.getBytecodeEND())
