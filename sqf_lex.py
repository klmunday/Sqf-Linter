import ply.lex as plex

reserved = {
    'for': 'FOR',
    'if': 'IF',
    'with': 'WITH',
    'while': 'WHILE',
    'switch': 'SWITCH',
    'private': 'PRIVATE',
    'else': 'ELSE',
#    'this': 'THIS',
#    'thislist': 'THISLIST',
#    'thistrigger': 'THISTRIGGER',
#    '_this': '_THIS',
#    '_x': '_X',
#    '_exception': '_EXCEPTION',
#    '_foreachindex': '_FOREACHINDEX',
#    '_thiseventhandler': '_THISEVENTHANDLER',
#    '_thisfsm': '_THISFSM',
#    '_thisscript': '_THISSCRIPT',
}

tokens = [
    'NUMBER_REAL',
    'NUMBER_HEX',
    'NUMBER_EXP',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'POW',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'LSPAREN',
    'RSPAREN',
    'COMMA',
    'SELECT',
    'PRIVATE_ID',
    'GLOBAL_ID',
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'NEWLINE',
    'SEMI_COLON',
    'COLON',
    'EQUAL',
    'LT',
    'GT',
    'AND',
    'OR',
    'NOT',
    'STRING_DOUBLE',
    'STRING_SINGLE',
    'BOOL',
] + list(reserved.values())

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_POW = r'\^'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSPAREN = r'\['
t_RSPAREN = r'\]'
t_COMMA = r','
t_SELECT = r'\#'
t_SEMI_COLON = r';'
t_COLON = r':'
t_EQUAL = r'='
t_BOOL = r'True|true|False|false'


def t_STRING_DOUBLE(t):
    r'\"\"|\"([^\"]+|\"{2,})+\"'
    t.lexer.lineno += t.value.count('\n')
    return t


def t_STRING_SINGLE(t):
    r"''|'([^']+|'{2,})+'"
    t.lexer.lineno += t.value.count('\n')
    return t


def t_COMMENT_SINGLE(t):
    r'//.*[\n\r]?'
    t.lexer.lineno += 1
    return t


def t_COMMENT_MULTI(t):
    r'/\*[\w\W]*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t


def t_PRIVATE_ID(t):
    r'_[a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'PRIVATE_ID')
    return t


def t_GLOBAL_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.lower(), 'GLOBAL_ID')
    return t


def t_NUMBER_EXP(t):
    r'([0-9]+\.)?[0-9]+[eE][-+]?[0-9]+'
    t.value = float(t.value)
    return t


def t_NUMBER_HEX(t):
    r'(\$|0x)[0-9a-fA-F]+'
    t.value = t.value.replace('$', '0x')
    t.value = int(t.value, base=16)
    return t


def t_NUMBER_REAL(t):
    r'\d*\.?\d+'
    t.value = float(t.value) if any([x in t.value for x in ['.', 'e', 'nan']]) else int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print(f'Illegal character "{t.value[0]}" on line {lexer.lineno}')
    t.lexer.skip(1)


lexer = plex.lex()


def lex():
    return lexer
