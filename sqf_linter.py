import sys
import sqf_lex
import sqf_yacc_fh


if __name__ == '__main__':
    if len(sys.argv) > 1:
        lexer = sqf_lex.lex()
        with open(sys.argv[1], 'r') as f:
            data = f.read()
        lexer.input(data)
        parser = sqf_yacc_fh.yacc()
        vars = parser.parse(lexer=lexer, debug=False)
        print(vars)
