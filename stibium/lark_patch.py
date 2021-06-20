'''
Monkey-patches made on lark, required until lark makes a new release.

As of 06/20/2021, Lark's master branch on Github has already implemented the functionality for
get_puppet(). So as soon as another release is made by Lark, this file may be deleted.

Author: Gary Geng
'''

from lark.lark import Lark
from lark.parsers.lalr_parser import ParserState, ParseConf
from lark.parsers.lalr_puppet import ParserPuppet
from lark.lexer import LexerThread



def get_puppet(lark_inst: Lark, start: str, text: str):
    '''HACK Generate a ParserPuppet without having encountered bugs.'''
    lalr_parser = lark_inst.parser.parser
    internal_parser = lalr_parser.parser
    lexer = lark_inst.parser.lexer
    lexer_thread = LexerThread(lexer, text)
    parse_conf = ParseConf(internal_parser.parse_table, internal_parser.callbacks, start)
    parser_state = ParserState(parse_conf, lexer_thread, None, None)
    return ParserPuppet(internal_parser, parser_state, parser_state.lexer)
