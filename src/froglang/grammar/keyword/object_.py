"""
object_.py
The Frog Programming Language Grammar: object

Development Leader: @RedoC
"""


class FrogOBJECT:
    """
    FrogOBJECT is the grammar class
    """

    def __init__(self, name: str):
        self.name = name

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin object
        :return:
        """
        commandcode = "(BEGINOBJECT ({})".format(self.name)    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end object
        :return:
        """
        commandcode = "ENDOBJECT)"    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    object_ = FrogOBJECT("foo")
    print(object_.getCommandcodeBegin())
    print(object_.getCommandcodeEND())

