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

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of import
        :return:
        """
        bytecode = "IMPORT ({})".format(self.module_name)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    import_ = FrogIMPORT("io")
    print(import_.getBytecode())
