import sys
from linter import sqf_lex, sqf_yacc
from contextlib import redirect_stdout
from classes.var_handler import VarHandler

global_var_handler = VarHandler()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            data = f.read()
        lexer = sqf_lex.lex()
        lexer.input(data)
        parser = sqf_yacc.yacc()
        debug = True
        results = parser.parse(lexer=lexer, debug=debug)
        if results:
            print(results)
