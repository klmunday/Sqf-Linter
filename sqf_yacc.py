import ply.yacc as pyacc
from sqf_lex import tokens
import sys


literals = []
variables = {}

precedence = (  # https://community.bistudio.com/wiki/SQF_syntax#Rules_of_Precedence
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'POW'),
    ('right', 'UMINUS')
)


def p_expressions(p):
    """
    expressions : expression SEMI_COLON expressions
                | expression SEMI_COLON
    """
    print(f'EXPRESSIONS: {" ".join(map(str, p))}')


def p_expression(p):
    """
    expression  : LPAREN expression RPAREN
                | expression operator expression
                | assignment
                | number
                | identifier
    """
    print(f'EXPRESSION: {" ".join(map(str, p))}')
    p[0] = eval(''.join(map(str, p[1:])))


def p_operator(p):
    """
    operator    : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MOD
                | POW
    """
    p[0] = p[1]


def p_expr_uminus(p):
    """
    expression : MINUS expression %prec UMINUS
    """
    print(f'EXPR_UMINUS: {" ".join(map(str, p))}')
    p[0] = -p[2]


def p_assignment(p):
    """
    assignment  : declaration EQUAL expression
                | PRIVATE_ID EQUAL expression
                | GLOBAL_ID EQUAL expression
    """
    print(f'ASSIGNMENT: {" ".join(map(str, p))}')
    value = variables.get(p[1], None)
    if value:
        variables[p[1]] = p[3]
        print(variables.items())
        p[0] = p[3]
    else:
        print(f'ERROR: variable {p[1]} undefined.', file=sys.stderr)
        pass


def p_declaration(p):
    """
    declaration : PRIVATE PRIVATE_ID
    """
    exists = variables.get(p[2], None)
    if exists:
        print(f'WARNING: variable {p[2]} already defined.', file=sys.stderr)
        pass
    else:
        variables[p[2]] = 'EMPTY'
        print(variables.items())
        p[0] = p[2]


def p_identifier(p):
    """
    identifier  : PRIVATE_ID
                | GLOBAL_ID
    """
    p[0] = p[1]


def p_number(p):
    """
    number  : NUMBER_REAL
            | NUMBER_HEX
            | NUMBER_EXP
    """
    print(f'NUMBER: {" ".join(map(str, p))}')
    p[0] = p[1]


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    if p:
        print('Syntax error in file. Unexpected "{}" at line#{}, pos#{}'.format(p.value, p.lineno, p.lexpos))
    else:
        print('Syntax error in file - Possibly an incomplete statement.')


parser = pyacc.yacc()


def yacc():
    return parser
