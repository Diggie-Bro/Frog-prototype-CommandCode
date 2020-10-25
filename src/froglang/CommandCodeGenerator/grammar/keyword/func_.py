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

    def getCommandcodeBegin(self):
        """
        getCommandcodeBegin(self)
        get commandcode of begin func
        :return:
        """
        commandcode = "BEGINFUNC ({funcname}%{param})".format(funcname=self.funcname, param=','.join([str(e) for e in self.param]))    # commandcode
        return commandcode

    def getCommandcodeEND(self):
        """
        getCommandcodeEND(self)
        get commandcode of end func
        :return:
        """
        commandcode = "ENDFUNC"    # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    func_ = FrogFUNC("func", ["foo", "boo"])
    print(func_.getCommandcodeBegin())
    print(func_.getCommandcodeEND())

