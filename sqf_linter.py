import sys
import sqf_lex
import sqf_yacc_fh
from contextlib import redirect_stdout


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open('output.log', 'w') as out_file:
            with redirect_stdout(out_file):
                lexer = sqf_lex.lex()
                with open(sys.argv[1], 'r') as f:
                    data = f.read()
                lexer.input(data)
                parser = sqf_yacc_fh.yacc()

                debug = False
                if debug:
                    sys.stderr = sys.stdout  # to put debug output
                results = parser.parse(lexer=lexer, debug=debug)
                print(results)
