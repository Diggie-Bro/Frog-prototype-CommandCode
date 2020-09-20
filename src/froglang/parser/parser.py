"""
parser.py
The Frog Programming Language Official Parser

Development Leader: @RedoC
"""

import copy
import src.froglang.grammar.operations as oper
import src.froglang.grammar.keywords as keywd


class Parser:
    """
    class Parser parse frogcode to bytecode
    """

    def __init__(self, linecode: str, bracketlist: list):
        """
        self.__init__(linecode)
        init class
        :param linecode:
        """
        self.linecode = linecode
        self.bracketlist = bracketlist

    def parse(self):
        """
        self.parse()
        parsing main method
        :return bytecode:
        """

        splited_code = self.linecode.split(" ")
        temp = []
        temp = copy.deepcopy(splited_code)

        # keyword check
        keyword = keywd.getKeyword(splited_code)

        temp.remove(keyword)
        # keyword ability check
        if keywd.getKeyword(temp) is not None:
            # :TODO MultiKeywordError handle
            pass

        # keyword grammar branch
        """
        code structure
        if keyword == keywd.keywordList[]:
        > bracket check
        > grammar check
        > operation convert
        > make bytecode
        """
        if keyword == keywd.keywordList[0]:  # import
            if len(splited_code) != 2:
                # :TODO GrammmarError handle
                pass
            grammar_class = keywd.keywordClassList[0]
            if splited_code.index(keyword) == 0:
                bytecode = grammar_class(splited_code[1]).getBytecode()
                return bytecode

            # :TODO GrammarError handle
        if keyword == keywd.keywordList[1]:  # main
            pass
        if keyword == keywd.keywordList[2]:  # func
            pass
        if keyword == keywd.keywordList[3]:  # object
            pass
        if keyword == keywd.keywordList[4]:  # var
            pass
        if keyword == keywd.keywordList[5]:  # for
            pass
        if keyword == keywd.keywordList[6]:  # if
            pass
        if keyword == keywd.keywordList[7]:  # try
            pass
        if keyword == keywd.keywordList[8]:  # except
            pass
        if keyword == keywd.keywordList[9]:  # const
            pass
        if keyword == keywd.keywordList[10]:  # return
            pass
        if keyword == keywd.keywordList[11]:  # else
            pass
        if keyword == keywd.keywordList[12]:  # elif
            pass


if __name__ == '__main__':
    parser = Parser("import io", [])
    print(parser.parse())
