import ply.yacc as pyacc
from sqf_lex import tokens


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]





parser = pyacc.yacc()


def yacc():
    return parser
