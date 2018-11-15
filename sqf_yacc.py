import ply.yacc as pyacc
from sqf_lex import tokens


literals = []


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS')
)


def p_expression(p):
    """
    expression  : expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | LPAREN expression RPAREN
                | number
    """
    p[0] = eval(''.join(map(str, p[1:])))


def p_expr_uminus(p):
    """
    expression : MINUS expression %prec UMINUS
    """
    p[0] = -p[2]


def p_number(p):
    """
    number  : NUMBER_REAL
            | NUMBER_HEX
            | NUMBER_EXP
    """
    p[0] = p[1]


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    if p:
        print('Syntax error in file. Unexpected {} at line:{}, pos:{}'.format(p.value, p.lineno, p.lexpos))
    else:
        print('Syntax error in file - Possibly an incomplete statement.')


parser = pyacc.yacc()


def yacc():
    return parser
