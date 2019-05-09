import sys
import sqf_lex
import sqf_yacc
from contextlib import redirect_stdout, redirect_stderr


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open('output.log', 'w') as out_file:
            with redirect_stdout(out_file):
                with open(sys.argv[1], 'r') as f:
                    data = f.read()
                lexer = sqf_lex.lex()
                lexer.input(data)
                parser = sqf_yacc.yacc()

                debug = False
                if debug:
                    sys.stderr = sys.stdout  # to put debug output
                results = parser.parse(lexer=lexer, debug=debug)
                print(results)
