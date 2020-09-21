"""
command-code.py
The Frog Programming Language Official Commandcode converter

Development Leader: @RedoC
"""

import copy
import re
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

    def setLinecode(self, linecode: str):
        """
        self.setLinecode(linecode)
        set linecode
        :param linecode:
        :return:
        """
        self.linecode = linecode

    def parse(self):
        """
        self.parse()
        parsing main method
        :return commandcode:
        """
        # code optimization
        parens = re.findall(r"\(([^)]+)", self.linecode)
        for i in range(len(parens)):
            self.linecode = self.linecode.replace(parens[i], parens[i].replace(" ", ""))

        splited_code = self.linecode.split(" ")
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
            """
                import <module_name>
            """
            if len(splited_code) != 2:
                # :TODO GrammmarError handle
                return

            grammar_class = keywd.keywordClassList[0]
            if splited_code.index(keyword) == 0:
                commandcode = grammar_class(splited_code[1]).getCommandcode()
                return commandcode

            # :TODO GrammarError handle
        if keyword == keywd.keywordList[1]:  # main
            """
                main {
            """
            if len(splited_code) != 2:
                # :TODO GrammmarError handles
                return

            grammar_class = keywd.keywordClassList[1]
            if splited_code.index(keyword) == 0 and splited_code[1] == '{':
                commandcode = grammar_class().getCommandcodeBegin()
                self.bracketlist.append("main")
                return commandcode
            # :TODO GrammmarError handles

        if keyword == keywd.keywordList[2]:  # func
            """
            func <funcname>(<params>) {
            """

            splited_code = self.linecode.split(" ")

            if len(splited_code) != 3:
                # :TODO GrammmarError handles
                return

            grammar_class = keywd.keywordClassList[2]
            if splited_code.index(keyword) == 0 and splited_code[2] == '{':
                if '(' in splited_code[1] and ')' in splited_code[1] \
                        and list(splited_code[1]).count('(') == 1 and list(splited_code[1]).count(')') == 1 \
                        and splited_code[1].index('(') < splited_code[1].index(')'):
                    commandcode = grammar_class(splited_code[1][:list(splited_code[1]).index('(')],
                                                re.findall(r"\(([^)]+)", splited_code[1])[0].split(',')).getCommandcodeBegin()
                    self.bracketlist.append("func")
                    return commandcode

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


# unit test
if __name__ == '__main__':
    parser = CommandCoder("", [])
    with open("../prototype/hello_world") as f:
        codes = f.readlines()
        for code in codes:
            parser.setLinecode(code[:-1])
            print(parser.parse())
