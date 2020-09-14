"""
mainfunc_.py
The Frog Programming Language Grammar: main

Development Leader: @RedoC
"""


class FrogMAIN:
    """
    FrogMAIN is the grammar class
    """

    def __init__(self):
        pass

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin main
        :return:
        """
        bytecode = "(BEGINMAIN"    # bytecode
        return bytecode

    def getBytecodeEnd(self):
        """
        getBytecodeEnd(self)
        get bytecode of end main
        :return:
        """
        bytecode = "ENDMAIN)"    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    main_ = FrogMAIN()
    print(main_.getBytecodeBegin())
    print(main_.getBytecodeEnd())

