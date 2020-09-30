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

        self.linecode = self.linecode.strip()
        parens = re.findall(r"\(([^)]+)", self.linecode)
        for i in range(len(parens)):
            self.linecode = self.linecode.replace(parens[i], parens[i].replace(" ", "\&SPACEPAREN"))

        strings = re.findall(r'["](.*?)["]', self.linecode)
        for i in range(len(strings)):
            self.linecode = self.linecode.replace(strings[i], strings[i]
                                                  .replace(" ", "\&SPACESTR")
                                                  .replace("\&SPACEPAREN", "\&SPACESTR")
                                                  )

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
        
        <> : necessary word
        [] : option
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
        elif keyword == keywd.keywordList[1]:  # main
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

        elif keyword == keywd.keywordList[2]:  # func
            """
                func <funcname>(<params>) {
            """

            if len(splited_code) != 3:
                # :TODO GrammmarError handles
                return

            grammar_class = keywd.keywordClassList[2]
            if splited_code.index(keyword) == 0 and splited_code[2] == '{':
                if '(' in splited_code[1] and ')' in splited_code[1] \
                        and list(splited_code[1]).count('(') == 1 and list(splited_code[1]).count(')') == 1 \
                        and splited_code[1].index('(') < splited_code[1].index(')'):
                    splited_code = [code_snipet.replace("\&SPACEPAREN", "") for code_snipet in splited_code]
                    commandcode = grammar_class(splited_code[1][:list(splited_code[1]).index('(')],
                                                re.findall(r"\(([^)]+)", splited_code[1])[0].split(
                                                    ',')).getCommandcodeBegin()
                    self.bracketlist.append("func")
                    return commandcode
            # :TODO GrammmarError handles

        elif keyword == keywd.keywordList[3]:  # object
            """
                object <objectname> {
            """
            if len(splited_code) != 3:
                # :TODO GrammmarError handles
                return

            grammar_class = keywd.keywordClassList[3]
            if splited_code.index(keyword) == 0 and splited_code[2] == '{':
                commandcode = grammar_class(splited_code[1]).getCommandcodeBegin()
                self.bracketlist.append("object")
                return commandcode
            # :TODO GrammmarError handles
        elif keyword == keywd.keywordList[4]:  # var
            """
                var <objectname> = <init>
            """
            if len(splited_code) < 4:
                # :TODO GrammmarError handles
                return
            # :TODO GrammmarError handles
            grammar_class = keywd.keywordClassList[4]
            if splited_code.index(keyword) == 0 and splited_code[2] == '=':
                commandcode = grammar_class(splited_code[1], ' '.join(splited_code[3:])).getCommandcode()
                return commandcode
        # :TODO GrammmarError handles

        elif keyword == keywd.keywordList[5]:  # for
            """
                for (<statement>) {
            """
            if len(splited_code) != 3:
                # :TODO GrammmarError handles
                return
            grammar_class = keywd.keywordClassList[5]
            if splited_code.index(keyword) == 0 and splited_code[2] == '{':
                if '(' in splited_code[1] and ')' in splited_code[1] \
                        and list(splited_code[1]).count('(') == 1 and list(splited_code[1]).count(')') == 1 \
                        and splited_code[1].index('(') < splited_code[1].index(')'):
                    splited_code = [code_snipet.replace("\&SPACEPAREN", "") for code_snipet in splited_code]
                    commandcode = grammar_class(
                        re.findall(r"\(([^)]+)", splited_code[1])[0]
                    ).getCommandcodeBegin()
                    self.bracketlist.append("for")
                    return commandcode
            # :TODO GrammmarError handles
        elif keyword == keywd.keywordList[6]:  # if
            """
                if <statement> {
            """
            pass
        elif keyword == keywd.keywordList[7]:  # try
            """
                try {
            """
            pass
        elif keyword == keywd.keywordList[8]:  # except
            """
                except [error] {
            """
            pass
        elif keyword == keywd.keywordList[9]:  # const
            """
                const <objectname> = <init>
            """
            pass
        elif keyword == keywd.keywordList[10]:  # return
            """
                return <value>
            """
            pass
        elif keyword == keywd.keywordList[11]:  # else
            """
                else {
            """
            pass
        elif keyword == keywd.keywordList[12]:  # elif
            """
                elif <statement> {
            """
            pass
        elif len(splited_code) == 1 and splited_code[0] == '}':  # end of bracket
            ended_keywd = self.bracketlist.pop()
            if ended_keywd == "main":
                commandcode = keywd.mainfunc_.FrogMAIN()
                return commandcode.getCommandcodeEnd()
            elif ended_keywd == "func":
                commandcode = keywd.func_.FrogFUNC("", [])
                return commandcode.getCommandcodeEND()
            elif ended_keywd == "object":
                commandcode = keywd.object_.FrogOBJECT("")
                return commandcode.getCommandcodeEND()
            elif ended_keywd == "for":
                commandcode = keywd.for_.FrogFOR("")
                return commandcode.getCommandcodeEND()


# unit test
if __name__ == '__main__':
    parser = CommandCoder("", [])
    with open("../prototype/hello_world") as f:
        codes = f.readlines()
        for code in codes:
            parser.setLinecode(code)
            print(parser.parse())
