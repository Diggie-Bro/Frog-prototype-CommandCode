"""
elif_.py
The Frog Programming Language Grammar: elif

Development Leader: @RedoC
"""


class FrogELIF:
    """
    FrogELIF is the grammar class
    """

    def __init__(self, statement: str):
        self.statement = statement

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin elif
        :return:
        """
        commandcode = "(BEGINELIF ({})".format(self.statement)    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end elif
        :return:
        """
        commandcode = "ENDELIF)".format(self.statement)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    elif_ = FrogELIF("foo > boo")
    print(elif_.getCommandcodeBegin())
    print(elif_.getCommandcodeEND())
