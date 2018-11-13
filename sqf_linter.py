import sys
import sqf_lex
import sqf_yacc


if __name__ == '__main__':
    if len(sys.argv) > 1:
        lexer = sqf_lex.lex()
        with open(sys.argv[1], 'r') as f:
            data = f.read()
            lexer.input(data)
            print('        (TYPE, VALUE, LINENO, LEXPOS)')
            for tok in lexer:
                print(tok)
