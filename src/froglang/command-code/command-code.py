"""
command-code.py
The Frog Programming Language Official Commandcode converter

Development Leader: @RedoC
"""

import copy
import src.froglang.grammar.operations as oper
import src.froglang.grammar.keywords as keywd


class CommandCoder:
    """
    class CommandCoder convert frogcode to commandcode
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
        :return commandcode:
        """

        splited_code = self.linecode.split(" ")
        temp = []
        temp = copy.deepcopy(splited_code)

        # keyword check
        keyword = keywd.getKeyword(splited_code)

        if keyword is not None:
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
        > make commandcode
        """
        if keyword == keywd.keywordList[0]:  # import
            if len(splited_code) != 2:
                # :TODO GrammmarError handle
                pass
            grammar_class = keywd.keywordClassList[0]
            if splited_code.index(keyword) == 0:
                commandcode = grammar_class(splited_code[1]).getcommandcode()
                return commandcode

            # :TODO GrammarError handle
        if keyword == keywd.keywordList[1]:  # main
            if len(splited_code) != 2:
                # :TODO GrammmarError handles
                pass
            grammar_class = keywd.keywordClassList[1]
            if splited_code.index(keyword) == 0 and splited_code[1] == '{':
                commandcode = grammar_class().getcommandcodeBegin()
                self.bracketlist.append("main")
                return commandcode

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
    parser = CommandCoder("import io", [])
    print(parser.parse())
    parser2 = CommandCoder("main{", [])
    print(parser2.parse())
