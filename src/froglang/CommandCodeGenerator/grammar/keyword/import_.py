"""
import_.py
The Frog Programming Language Grammar: import

Development Leader: @RedoC
"""


class FrogIMPORT:
    """
    FrogIMPORT is the grammar class
    """

    def __init__(self, module_name: str):
        self.module_name = module_name

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of import
        :return:
        """
        commandcode = "IMPORT ({})".format(self.module_name)    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    import_ = FrogIMPORT("io")
    print(import_.getCommandcode())
