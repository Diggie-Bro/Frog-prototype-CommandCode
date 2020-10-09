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

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin try
        :return:
        """
        commandcode = "BEGINTRY"    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end try
        :return:
        """
        commandcode = "ENDTRY"    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    try_ = FrogTRY()
    print(try_.getCommandcodeBegin())
    print(try_.getCommandcodeEND())
