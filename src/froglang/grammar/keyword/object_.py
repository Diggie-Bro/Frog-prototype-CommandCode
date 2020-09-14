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

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin object
        :return:
        """
        bytecode = "(BEGINOBJECT ({})".format(self.name)    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end object
        :return:
        """
        bytecode = "ENDOBJECT)"    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    object_ = FrogOBJECT("foo")
    print(object_.getBytecodeBegin())
    print(object_.getBytecodeEND())

