"""
parser.py
The Frog Programming Language Official Parser

Development Leader: @RedoC
"""

import src.froglang.grammar.operations as oper
import src.froglang.grammar.keywords as keywd


class Parser:
    """
    class Parser parse frogcode to bytecode
    """

    def __init__(self, linecode):
        """
        self.__init__(linecode)
        init class
        :param linecode:
        """
        self.linecode = linecode

    def parse(self):
        """
        self.parse()
        parsing main method
        :return:
        """
