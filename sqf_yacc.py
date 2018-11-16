import ply.yacc as pyacc
from sqf_lex import tokens


literals = []
variables = set()

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
                | expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | expression MOD expression
                | expression POW expression
                | assignment
                | number
                | identifier
    """
    print(f'EXPRESSION: {" ".join(map(str, p))}')
    p[0] = eval(''.join(map(str, p[1:])))


def p_expr_uminus(p):
    """
    expression : MINUS expression %prec UMINUS
    """
    print(f'EXPR_UMINUS: {" ".join(map(str, p))}')
    p[0] = -p[2]


def p_assignment(p):
    """
    assignment  : PRIVATE PRIVATE_ID EQUAL expression
                | GLOBAL_ID EQUAL expression
    """
    print(f'ASSIGNMENT: {" ".join(map(str, p))}')
    if len(p) > 4:
        p[0] = p[4]
    else:
        p[0] = p[3]


def p_identifier(p):
    """
    identifier  : PRIVATE_ID
                | GLOBAL_ID
    """
    variables.add(p[1])
    print(variables)
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
