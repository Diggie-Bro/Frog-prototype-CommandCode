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

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin main
        :return:
        """
        commandcode = "(BEGINMAIN"    # commandcode
        return commandcode

    def getCommandcodeEnd(self):
        """
        getCommandcodeEnd(self)
        get commandcode of end main
        :return:
        """
        commandcode = "ENDMAIN)"    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    main_ = FrogMAIN()
    print(main_.getCommandcodeBegin())
    print(main_.getCommandcodeEnd())

