"""
keywords.py
The Frog Programming Language Grammar: Keyword

Development Leader: @RedoC
"""

import grammar.keyword.import_ as import_
import grammar.keyword.mainfunc_ as mainfunc_
import grammar.keyword.func_ as func_
import grammar.keyword.object_ as object_
import grammar.keyword.var_ as var_
import grammar.keyword.for_ as for_
import grammar.keyword.if_ as if_
import grammar.keyword.try_ as try_
import grammar.keyword.except_ as except_
import grammar.keyword.const_ as const_
import grammar.keyword.return_ as return_
import grammar.keyword.else_ as else_
import grammar.keyword.elif_ as elif_
import grammar.keyword.callfunc as cfunc_

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
    'elif',
    'run'
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
    elif_.FrogELIF,
    cfunc_.CALLFUNC
)


def getKeyword(wordlist):
    """
    isKeyword(word)
    check is 'wordlist' in keywordlist
    :param wordlist:
    :return:
    """
    for word in wordlist:
        for keywd in keywordList:
            if word == keywd:
                return keywd

    return None
