"""
return_.py
The Frog Programming Language Grammar: return

Development Leader: @RedoC
"""


class FrogRETURN:
    """
    FrogRETURN is the grammar class
    """

    def __init__(self, value: str):
        self.value = value

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of return
        :return:
        """
        commandcode = "RETURN ({})".format(self.value)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    return_ = FrogRETURN("result")
    print(return_.getCommandcode())

