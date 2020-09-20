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

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin if
        :return:
        """
        commandcode = "(BEGINIF ({})".format(self.statement)    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end if
        :return:
        """
        commandcode = "ENDIF)".format(self.statement)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    if_ = FrogIF("foo > boo")
    print(if_.getCommandcodeBegin())
    print(if_.getCommandcodeEND())

