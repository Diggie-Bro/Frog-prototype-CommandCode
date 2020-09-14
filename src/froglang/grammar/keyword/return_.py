"""
return_.py
The Frog Programming Language Grammar: return

Development Leader: @RedoC
"""


class FrogRETURN:
    """
    FrogRETURN is the grammar class
    """

    def __init__(self, value: str):
        self.value = value

    def getBytecode(self):
        """
        getBytecode(self)
        get bytecode of return
        :return:
        """
        bytecode = "RETURN ({})".format(self.value)    # bytecode
        return bytecode


if __name__ == '__main__':
    # unit test
    return_ = FrogRETURN("result")
    print(return_.getBytecode())

