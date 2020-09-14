"""
dot.py
The Frog Programming Language Operation: dot(Object.method or Object.var)

Development Leader: @RedoC
"""


class DOT:
    """
    DOT is the operation class
    >> example
    objectname.foo()
    foo.boo
    """

    def __init__(self, pipeline: list):
        self.pipeline = pipeline

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of dot expr
        :return:
        """
        bytecode = "DOT ({})".format(".".join([str(e) for e in self.pipeline]))  # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    dot_ = DOT(["objectname", "foo()"])
    print(dot_.getBytecode())
