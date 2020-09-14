"""
func_.py
The Frog Programming Language Grammar: func

Development Leader: @RedoC
"""


class FrogFUNC:
    """
    FrogFUNC is the grammar class
    """

    def __init__(self, funcname: str, param: list):
        self.param = param
        self.funcname = funcname

    def getBytecodeBegin(self):
        """
        getBytecodeBegin(self)
        get bytecode of begin func
        :return:
        """
        bytecode = "(BEGINFUNC ({funcname}<={param})".format(funcname=self.funcname, param=' '.join([str(e) for e in self.param]))    # bytecode
        return bytecode

    def getBytecodeEND(self):
        """
        getBytecodeEND(self)
        get bytecode of end func
        :return:
        """
        bytecode = "ENDFUNC)".format(self.param)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    func_ = FrogFUNC("func", ["foo", "boo"])
    print(func_.getBytecodeBegin())
    print(func_.getBytecodeEND())

