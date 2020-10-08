"""
callfunc.py
The Frog Programming Language Operation & Keyword: call (func)

Development Leader: @RedoC
"""


class CALLFUNC:
    """
    CALLFUNC is the multi class
    >> example
    run foo(boo)
    run print("")
    """

    def __init__(self, funcname: str, param: list):
        self.funcname = funcname
        self.param = param

    def getCommandcode(self):
        """
        getCommandcode(self)
        get commandcode of function calling
        :return:
        """
        commandcode = "CALL ({funcname})({param})".format(funcname=self.funcname, param=",".join([str(e) for e in self.param]))   # commandcode
        return commandcode


if __name__ == '__main__':
    # unit test
    assign_ = CALLFUNC("print", ["hello, world!"])
    print(assign_.getCommandcode())
