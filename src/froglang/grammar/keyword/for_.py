"""
for_.py
The Frog Programming Language Grammar: for

Development Leader: @RedoC
"""


class FrogFOR:
    """
    FrogFOR is the grammar class
    """

    def __init__(self, statement: str):
        self.statement = statement

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin for
        :return:
        """
        commandcode = "(BEGINFOR ({})".format(self.statement)    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end for
        :return:
        """
        commandcode = "ENDFOR)".format(self.statement)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    for_ = FrogFOR("foo > boo")
    print(for_.getCommandcodeBegin())
    print(for_.getCommandcodeEND())
