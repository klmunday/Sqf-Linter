import ply.yacc as pyacc
from sqf_lex import tokens

precedence = (
    ('left', 'OR', 'AND'),
    ('left', 'EQUALITY', 'INEQUALITY', 'LT', 'GT', 'LTE', 'GTE'),
    ('left', 'COLON'),
    #('left', 'BINARYOP', 'COLON'),
    ('left', 'ELSE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
    ('left', 'POW'),
    #('left', ''),   # array select
    #('left', 'UNARYOP'),  # LOGICALNOT likely wrong
    #('left', ''),
)


def p_code(p):
    """
    code                : statements
                        | statement
    """


def p_statements(p):
    """
    statements          : statement SEMI_COLON statement
                        | statement
    """


def p_statement(p):
    """
    statement           : empty
                        | assignment
                        | binaryexpression
    """


def p_assignment(p):
    """
    assignment          : PRIVATE identifier EQUAL binaryexpression
                        | identifier EQUAL binaryexpression
    """


def p_binaryexpression(p):
    """
    binaryexpression    : binaryexpression operator binaryexpression
                        | primaryexpression
    """


def p_primaryexpression(p):
    """
    primaryexpression   : number
                        | unaryexpression
                        | nularexpression
                        | variable
                        | string
                        | LBRACE code RBRACE
                        | LPAREN binaryexpression RPAREN
                        | array
    """


def p_array(p):
    """
    array               :  LSPAREN binaryexpression COMMA binaryexpression COMMA binaryexpression COMMA binaryexpression RSPAREN
                        | LSPAREN empty RSPAREN
    """


def p_nularexpression(p):
    """
    nularexpression     : operator
                        | empty
    """


def p_unaryexpression(p):
    """
    unaryexpression     : operator primaryexpression
                        | NOT primaryexpression
                        | empty
    """


def p_identifier(p):
    """
    identifier          : PRIVATE_ID
                        | GLOBAL_ID
    """


def p_variable(p):
    """
    variable            : identifier
    """


def p_operator(p):
    """
    operator            : identifier
                        | punctuation
    """


def p_punctuation(p):
    """
    punctuation         : DIVIDE
                        | MINUS
                        | MOD
                        | PLUS
                        | POW
                        | SELECT
                        | TIMES
                        | COLON
    """


def p_number(p):
    """
    number              : NUMBER_REAL
                        | NUMBER_HEX
                        | NUMBER_EXP
    """


def p_string(p):
    """
    string              : STRING_SINGLE
                        | STRING_DOUBLE
    """


def p_gte(p):
    """
    gte                 : GT EQUAL          %prec GTE
    """


def p_lte(p):
    """
    lte                 : LT EQUAL          %prec LTE
    """


def p_equality(p):
    """
    equality            : EQUAL EQUAL       %prec EQUALITY
    """


def p_inequality(p):
    """
    inequality          : NOT EQUAL         %prec INEQUALITY
    """


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    print('Syntax error in file')


parser = pyacc.yacc()


def yacc():
    return parser
