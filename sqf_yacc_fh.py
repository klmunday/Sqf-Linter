import ply.yacc as pyacc
from sqf_lex import tokens
import sys


literals = []
variables = {}

precedence = (  # https://community.bistudio.com/wiki/SQF_syntax#Rules_of_Precedence
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'POW'),
)


def p_code(p):
    """
    code    : statement
            | statement SEMI_COLON code
            | empty
    """
    p[0] = p[1]


def p_statement(p):
    """
    statement   : empty
                | assignment
                | binaryexp
    """
    p[0] = p[1]


def p_assignment(p):
    """
    assignment : identifier
                | binaryexp
                | PRIVATE identifier EQUAL binaryexp
    """
    p[0] = p[1]  # needs changing for last match


def p_binaryexp(p):
    """
    binaryexp   : binaryexp operator binaryexp
                | primaryexp
    """
    if len(p) > 1:
        p[0] = eval(''.join(map(str, p[1:])))
    else:
        p[0] = p[1]


def p_primaryexp(p):
    """
    primaryexp : number
                | unaryexp
                | nularexp
                | variable
                | string
                | LBRACE code RBRACE
                | LPAREN binaryexp RPAREN
                | LSPAREN RSPAREN
                | LSPAREN arrayelement RSPAREN
    """


def p_arrayelement(p):
    """
    arrayelement    : binaryexp
                    | binaryexp COMMA arrayelement
    """


def p_nularexp(p):
    """
    nularexp : operator
    """
    p[0] = p[1]


def unaryexp(p):
    """
    unaryexp    : operator
                | primaryexp
    """
    p[0] = p[1]


def p_operator(p):
    """
    operator    : identifier
                | punctuation
    """
    p[0] = p[1]


def p_identifier(p):
    """
    identifier  : PRIVATE_ID
                | GLOBAL_ID
    """
    p[0] = p[1]


def p_number(p):
    """
    number  : NUMBER_REAL
            | NUMBER_EXP
            | NUMBER_HEX
    """
    p[0] = p[1]


def p_string(p):
    """
    string  : STRING_SINGLE
            | STRING_DOUBLE
    """
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
