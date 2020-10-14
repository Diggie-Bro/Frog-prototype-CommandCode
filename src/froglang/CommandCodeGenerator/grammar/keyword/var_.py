"""
var_.py
The Frog Programming Language Grammar: var

Development Leader: @RedoC
"""


class FrogVAR:
    """
    FrogVAR is the grammar class
    """

    def __init__(self, name: str, init=None):
        self.name = name
        self.init = init

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of var
        :return:
        """
        commandcode = "VAR ({name})({init})".format(name=self.name, init=self.init)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    var = FrogVAR("foo", 36)
    print(var.getCommandcode())
