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

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin else
        :return:
        """
        commandcode = "(BEGINELSE"    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end else
        :return:
        """
        commandcode = "ENDELSE)"    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    else_ = FrogELSE()
    print(else_.getCommandcodeBegin())
    print(else_.getCommandcodeEND())
