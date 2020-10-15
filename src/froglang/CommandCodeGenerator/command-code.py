"""
command-code.py
The Frog Programming Language Official Commandcode converter

Development Leader: @RedoC
"""

import copy
import re
import grammar.operations as oper
import grammar.keywords as keywd


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

    def parseKeywd(self):
        """
        self.parseKeywd()
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
            if len(splited_code) != 4:
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
                if (<statement>) {
            """
            if len(splited_code) != 3:
                # :TODO GrammmarError handles
                return
            grammar_class = keywd.keywordClassList[6]
            if splited_code.index(keyword) == 0 and splited_code[2] == '{':
                if '(' in splited_code[1] and ')' in splited_code[1] \
                        and list(splited_code[1]).count('(') == 1 and list(splited_code[1]).count(')') == 1 \
                        and splited_code[1].index('(') < splited_code[1].index(')'):
                    splited_code = [code_snipet.replace("\&SPACEPAREN", "") for code_snipet in splited_code]
                    commandcode = grammar_class(
                        re.findall(r"\(([^)]+)", splited_code[1])[0]
                    ).getCommandcodeBegin()
                    self.bracketlist.append("if")
                    return commandcode
            # :TODO GrammmarError handles
            return
        elif keyword == keywd.keywordList[7]:  # try
            """
                try {
            """
            if len(splited_code) != 2:
                # :TODO GrammmarError handles
                return

            grammar_class = keywd.keywordClassList[7]
            if splited_code.index(keyword) == 0 and splited_code[1] == '{':
                commandcode = grammar_class().getCommandcodeBegin()
                self.bracketlist.append("try")
                return commandcode
            # :TODO GrammmarError handles
        elif keyword == keywd.keywordList[8]:  # except
            """
                except {
            """
            if len(splited_code) != 2:
                # :TODO GrammmarError handles
                return

            grammar_class = keywd.keywordClassList[8]
            if splited_code.index(keyword) == 0 and splited_code[1] == '{':
                commandcode = grammar_class().getCommandcodeBegin()
                self.bracketlist.append("except")
                return commandcode
            # :TODO GrammmarError handles
        elif keyword == keywd.keywordList[9]:  # const
            """
                const <objectname> = <init>
            """
            if len(splited_code) != 4:
                # :TODO GrammmarError handles
                return
            grammar_class = keywd.keywordClassList[9]
            if splited_code.index(keyword) == 0 and splited_code[2] == '=':
                commandcode = grammar_class(splited_code[1], ' '.join(splited_code[3:])).getCommandcode()
                return commandcode
            # :TODO GrammmarError handles
        elif keyword == keywd.keywordList[10]:  # return
            """
                return <value>
            """
            if len(splited_code) != 2:
                # :TODO GrammmarError handles
                return
            grammar_class = keywd.keywordClassList[10]
            if splited_code.index(keyword) == 0:
                commandcode = grammar_class(splited_code[1]).getCommandcode()
                return commandcode
            # :TODO GrammmarError handles
        elif keyword == keywd.keywordList[11]:  # else
            """
                else {
            """
            if len(splited_code) != 2 or not splited_code.index(keyword) == 0 or not splited_code[1] == "{":
                # :TODO GrammmarError handles
                return
            commandcode = keywd.keywordClassList[11]().getCommandcodeBegin()
            self.bracketlist.append("else")
            return commandcode
        elif keyword == keywd.keywordList[12]:  # elif
            """
                elif <statement> {
            """
            if len(splited_code) != 3:
                # :TODO GrammmarError handles
                return
            grammar_class = keywd.keywordClassList[12]
            if splited_code.index(keyword) == 0 and splited_code[2] == '{':
                if '(' in splited_code[1] and ')' in splited_code[1] \
                        and list(splited_code[1]).count('(') == 1 and list(splited_code[1]).count(')') == 1 \
                        and splited_code[1].index('(') < splited_code[1].index(')'):
                    splited_code = [code_snipet.replace("\&SPACEPAREN", "") for code_snipet in splited_code]
                    commandcode = grammar_class(
                        re.findall(r"\(([^)]+)", splited_code[1])[0]
                    ).getCommandcodeBegin()
                    self.bracketlist.append("elif")
                    return commandcode
            # :TODO GrammmarError handles
            return
        elif keyword == keywd.keywordList[13]:  # run
            """
            run <funcname>([param])
            """
            if len(splited_code) != 2:
                # :TODO GrammmarError handles
                return
            grammar_class = keywd.keywordClassList[13]
            if splited_code.index(keyword) == 0:
                if '(' in splited_code[1] and ')' in splited_code[1] \
                        and list(splited_code[1]).count('(') == 1 and list(splited_code[1]).count(')') == 1 \
                        and splited_code[1].index('(') < splited_code[1].index(')'):
                    splited_code = [code_snipet.replace("\&SPACEPAREN", "") for code_snipet in splited_code]
                    commandcode = grammar_class(
                        ''.join(list(splited_code[1])[:list(splited_code[1]).index("(")]),
                        re.findall(r"\(([^)]+)", splited_code[1])[0].split(',')
                    ).getCommandcode()
                    return commandcode
            # :TODO GrammmarError handles
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
            elif ended_keywd == "if":
                commandcode = keywd.if_.FrogIF("")
                return commandcode.getCommandcodeEND()
            elif ended_keywd == "try":
                commandcode = keywd.try_.FrogTRY()
                return commandcode.getCommandcodeEND()
            elif ended_keywd == "except":
                commandcode = keywd.except_.FrogEXCEPT()
                return commandcode.getCommandcodeEND()
            elif ended_keywd == "else":
                commandcode = keywd.else_.FrogELSE()
                return commandcode.getCommandcodeEND()
            elif ended_keywd == "elif":
                commandcode = keywd.elif_.FrogELIF("")
                return commandcode.getCommandcodeEND()
        else:
            # :TODO non-keyword operations.
            if "=" in splited_code:
                """
                <operand1> = <operand2>
                """
                if len(splited_code) != 3:
                    # :TODO GrammmarError handles
                    return

                grammar_class = oper.operationClassList[0]
                if splited_code.index('=') == 1:
                    commandcode = grammar_class(splited_code[0], splited_code[2])\
                        .getCommandcode()
                    return commandcode

    def parseDetail(self, l1code):
        """
        self.parseDetail(self, l1code)
        :param l1code
        parse more detail.
        """

        isNowString = False
        parens = re.findall(r"\(([^)]+)", l1code)

        for paren in parens:
            for charindex in range(len(list(paren))):
                if paren[charindex] is '"':
                    isNowString = False if isNowString == True else True
                if paren[charindex] is '=' and not isNowString:
                    """
                    available

                    == ('=' was already proceded.)
                    """
                    if paren[charindex + 1] == '=' and paren[charindex + 2] != '=': # ==
                        grammar_class = oper.operationClassList[5]
                        l2commandcode = grammar_class(paren[:charindex], paren[charindex + 2:])\
                            .getCommandcode()
                        l1code = l1code.replace(paren, l2commandcode)
        return l1code


# unit test
if __name__ == '__main__':
    generator = CommandCoder("", [])
    with open("../prototype/hello_world") as f:
        codes = f.readlines()
        for code in codes:
            generator.setLinecode(code)
            level_1_commandcode = "" if generator.parseKeywd() is None else generator.parseKeywd()
            print(generator.parseDetail(level_1_commandcode))

