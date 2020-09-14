"""
keywords.py
The Frog Programming Language Grammar: Keyword

Development Leader: @RedoC
"""

import src.froglang.grammar.keyword.import_ as import_
import src.froglang.grammar.keyword.mainfunc_ as mainfunc_
import src.froglang.grammar.keyword.func_ as func_
import src.froglang.grammar.keyword.object_ as object_
import src.froglang.grammar.keyword.var_ as var_
import src.froglang.grammar.keyword.for_ as for_
import src.froglang.grammar.keyword.if_ as if_
import src.froglang.grammar.keyword.try_ as try_
import src.froglang.grammar.keyword.except_ as except_
import src.froglang.grammar.keyword.const_ as const_
import src.froglang.grammar.keyword.return_ as return_
import src.froglang.grammar.keyword.else_ as else_
import src.froglang.grammar.keyword.elif_ as elif_

# keyword
keywordList = (
    'import',
    'main',
    'func',
    'object',
    'var',
    'for',
    'if',
    'try',
    'except',
    'const',
    'return',
    'else',
    'elif'
)

keywordClassList = (
    import_.FrogIMPORT,
    mainfunc_.FrogMAIN,
    func_.FrogFUNC,
    object_.FrogOBJECT,
    var_.FrogVAR,
    for_.FrogFOR,
    if_.FrogIF,
    try_.FrogTRY,
    except_.FrogEXCEPT,
    const_.FrogCONST,
    return_.FrogRETURN,
    else_.FrogELSE,
    elif_.FrogELIF
)


def getKeyword(word):
    """
    isKeyword(word)
    check is 'word' in keywordlist
    :param word:
    :return:
    """
    for keyword in keywordList:
        if keyword in word:
            return keyword

    return None
