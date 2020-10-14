"""
except_.py
The Frog Programming Language Grammar: except

Development Leader: @RedoC
"""


class FrogEXCEPT:
    """
    FrogEXCEPT is the grammar class
    """

    def __init__(self, error: str = None):
        self.error = error

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin except
        :return:
        """
        commandcode = "BEGINEXCEPT ({})".format(self.error)    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end except
        :return:
        """
        commandcode = "ENDEXCEPT"    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    except_ = FrogEXCEPT("StackOverflow")
    print(except_.getCommandcodeBegin())
    print(except_.getCommandcodeEND())
