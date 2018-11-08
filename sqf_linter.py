import sys
import ply.lex as lex


reserved = {
    'for': 'FOR',
    'if': 'IF',
    'with': 'WITH',
    'while': 'WHILE',
    'switch': 'SWITCH',
    'this': 'THIS',
    'thisList': 'THISLIST',
    'thisTrigger': 'THISTRIGGER',
    '_this': '_THIS',
    '_x': '_X',
    '_exception': '_EXCEPTION',
    '_forEachIndex': '_FOREACHINDEX',
    '_thisEventHandler': '_THISEVENTHANDLER',
    '_thisFSM': '_THISFSM',
    '_thisScript': '_THISSCRIPT',
}

tokens = [
    'NUMBER_REAL',
    'NUMBER_HEX',
    'NUMBER_EXP',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'NEWLINE',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


def t_COMMENT_SINGLE(t):
    r'//.*(\n)?'
    t.lexer.lineno += 1
    return t


def t_COMMENT_MULTI(t):
    r'/\*[\w\W]*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_NUMBER_EXP(t):
    r'([0-9]+\.)?[0-9]+e[-+]?[0-9]+'
    t.value = float(t.value)
    return t


def t_NUMBER_HEX(t):
    r'(\$|0x)[0-9a-f]+'
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


if __name__ == '__main__':
    lexer = lex.lex()
    with open('test.sqf', 'r') as f:
        data = f.read()
        lexer.input(data)
        print('        (TYPE, VALUE, LINENO, LEXPOS)')
        for tok in lexer:
            print(tok)
