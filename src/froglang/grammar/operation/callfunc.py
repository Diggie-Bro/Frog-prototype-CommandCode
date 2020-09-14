"""
callfunc.py
The Frog Programming Language Operation: call (func)

Development Leader: @RedoC
"""


class CALLFUNC:
    """
    CALLFUNC is the operation class
    >> example
    foo(boo)
    print("")
    """

    def __init__(self, funcname: str, param: list):
        self.funcname = funcname
        self.param = param

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of function calling
        :return:
        """
        bytecode = "CALL ({funcname})({param})".format(funcname=self.funcname, param=",".join([str(e) for e in self.param]))   # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    assign_ = CALLFUNC("print", ["hello, world!"])
    print(assign_.getBytecode())
