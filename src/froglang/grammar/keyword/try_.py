"""
try_.py
The Frog Programming Language Grammar: try

Development Leader: @RedoC
"""


class FrogTRY:
    """
    FrogTRY is the grammar class
    """

    def __init__(self):
        pass

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin try
        :return:
        """
        bytecode = "(BEGINTRY"    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end try
        :return:
        """
        bytecode = "ENDTRY)"    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    try_ = FrogTRY()
    print(try_.getBytecodeBegin())
    print(try_.getBytecodeEND())
