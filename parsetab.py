
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORANDleftEQUALITYINEQUALITYLTGTLTEGTEleftCOLONleftELSEleftPLUSMINUSleftTIMESDIVIDEMODleftPOWAND BOOL COLON COMMA COMMENT_MULTI COMMENT_SINGLE DIVIDE ELSE EQUAL FOR GLOBAL_ID GT IF LBRACE LPAREN LSPAREN LT MINUS MOD NEWLINE NOT NUMBER_EXP NUMBER_HEX NUMBER_REAL OR PLUS POW PRIVATE PRIVATE_ID RBRACE RPAREN RSPAREN SELECT SEMI_COLON STRING_DOUBLE STRING_SINGLE SWITCH TIMES WHILE WITH\n    code                : statements\n                        | statement\n    \n    statements          : statement SEMI_COLON statement\n                        | statement\n    \n    statement           : empty\n                        | assignment\n                        | binaryexpression\n    \n    assignment          : PRIVATE identifier EQUAL binaryexpression\n                        | identifier EQUAL binaryexpression\n    \n    binaryexpression    : binaryexpression operator binaryexpression\n                        | primaryexpression\n    \n    primaryexpression   : number\n                        | unaryexpression\n                        | nularexpression\n                        | variable\n                        | string\n                        | LBRACE code RBRACE\n                        | LPAREN binaryexpression RPAREN\n                        | array\n    \n    array               :  LSPAREN binaryexpression COMMA binaryexpression COMMA binaryexpression COMMA binaryexpression RSPAREN\n                        | LSPAREN empty RSPAREN\n    \n    nularexpression     : operator\n                        | empty\n    \n    unaryexpression     : operator primaryexpression\n                        | NOT primaryexpression\n                        | empty\n    \n    identifier          : PRIVATE_ID\n                        | GLOBAL_ID\n    \n    variable            : identifier\n    \n    operator            : identifier\n                        | punctuation\n    \n    punctuation         : DIVIDE\n                        | MINUS\n                        | MOD\n                        | PLUS\n                        | POW\n                        | SELECT\n                        | TIMES\n                        | COLON\n    \n    number              : NUMBER_REAL\n                        | NUMBER_HEX\n                        | NUMBER_EXP\n    \n    string              : STRING_SINGLE\n                        | STRING_DOUBLE\n    \n    gte                 : GT EQUAL          %prec GTE\n    \n    lte                 : LT EQUAL          %prec LTE\n    \n    equality            : EQUAL EQUAL       %prec EQUALITY\n    \n    inequality          : NOT EQUAL         %prec INEQUALITY\n    \n    empty :\n    '
    
_lr_action_items = {'SEMI_COLON':([0,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,38,39,41,42,43,44,47,51,52,53,54,55,57,58,64,],[-49,37,-5,-6,-7,-29,-22,-11,-27,-28,-12,-13,-14,-15,-16,-49,-19,-40,-41,-42,-49,-43,-44,-31,-32,-33,-34,-35,-36,-37,-38,-39,-49,-30,-49,-24,-23,-29,-25,-10,-49,-9,-17,-18,-21,-8,-20,]),'$end':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,47,50,51,52,53,54,55,57,58,64,],[-49,0,-1,-2,-5,-6,-7,-29,-22,-11,-27,-28,-12,-13,-14,-15,-16,-19,-40,-41,-42,-49,-43,-44,-31,-32,-33,-34,-35,-36,-37,-38,-39,-49,-49,-30,-49,-24,-23,-29,-25,-3,-10,-49,-9,-17,-18,-21,-8,-20,]),'PRIVATE_ID':([0,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[11,-23,11,11,-29,11,-11,-27,-28,-12,-13,-14,-15,-16,11,11,-19,-40,-41,-42,11,-43,-44,11,-31,-32,-33,-34,-35,-36,-37,-38,-39,11,11,-30,11,-24,-23,-29,11,-25,11,-23,11,11,11,-17,-18,11,-21,11,11,11,11,11,11,-20,]),'GLOBAL_ID':([0,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[12,-23,12,12,-29,12,-11,-27,-28,-12,-13,-14,-15,-16,12,12,-19,-40,-41,-42,12,-43,-44,12,-31,-32,-33,-34,-35,-36,-37,-38,-39,12,12,-30,12,-24,-23,-29,12,-25,12,-23,12,12,12,-17,-18,12,-21,12,12,12,12,12,12,-20,]),'DIVIDE':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[29,-23,29,-29,29,-11,-27,-28,-12,-13,-14,-15,-16,29,29,-19,-40,-41,-42,29,-43,-44,29,-31,-32,-33,-34,-35,-36,-37,-38,-39,29,29,-30,29,-24,-23,-29,29,-25,29,-23,29,29,29,-17,-18,29,-21,29,29,29,29,29,29,-20,]),'MINUS':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[30,-23,30,-29,30,-11,-27,-28,-12,-13,-14,-15,-16,30,30,-19,-40,-41,-42,30,-43,-44,30,-31,-32,-33,-34,-35,-36,-37,-38,-39,30,30,-30,30,-24,-23,-29,30,-25,30,-23,30,30,30,-17,-18,30,-21,30,30,30,30,30,30,-20,]),'MOD':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[31,-23,31,-29,31,-11,-27,-28,-12,-13,-14,-15,-16,31,31,-19,-40,-41,-42,31,-43,-44,31,-31,-32,-33,-34,-35,-36,-37,-38,-39,31,31,-30,31,-24,-23,-29,31,-25,31,-23,31,31,31,-17,-18,31,-21,31,31,31,31,31,31,-20,]),'PLUS':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[32,-23,32,-29,32,-11,-27,-28,-12,-13,-14,-15,-16,32,32,-19,-40,-41,-42,32,-43,-44,32,-31,-32,-33,-34,-35,-36,-37,-38,-39,32,32,-30,32,-24,-23,-29,32,-25,32,-23,32,32,32,-17,-18,32,-21,32,32,32,32,32,32,-20,]),'POW':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[33,-23,33,-29,33,-11,-27,-28,-12,-13,-14,-15,-16,33,33,-19,-40,-41,-42,33,-43,-44,33,-31,-32,-33,-34,-35,-36,-37,-38,-39,33,33,-30,33,-24,-23,-29,33,-25,33,-23,33,33,33,-17,-18,33,-21,33,33,33,33,33,33,-20,]),'SELECT':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[34,-23,34,-29,34,-11,-27,-28,-12,-13,-14,-15,-16,34,34,-19,-40,-41,-42,34,-43,-44,34,-31,-32,-33,-34,-35,-36,-37,-38,-39,34,34,-30,34,-24,-23,-29,34,-25,34,-23,34,34,34,-17,-18,34,-21,34,34,34,34,34,34,-20,]),'TIMES':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[35,-23,35,-29,35,-11,-27,-28,-12,-13,-14,-15,-16,35,35,-19,-40,-41,-42,35,-43,-44,35,-31,-32,-33,-34,-35,-36,-37,-38,-39,35,35,-30,35,-24,-23,-29,35,-25,35,-23,35,35,35,-17,-18,35,-21,35,35,35,35,35,35,-20,]),'COLON':([0,4,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47,48,49,51,52,53,54,55,56,57,58,59,60,61,62,63,64,],[36,-23,36,-29,36,-11,-27,-28,-12,-13,-14,-15,-16,36,36,-19,-40,-41,-42,36,-43,-44,36,-31,-32,-33,-34,-35,-36,-37,-38,-39,36,36,-30,36,-24,-23,-29,36,-25,36,-23,36,36,36,-17,-18,36,-21,36,36,36,36,36,36,-20,]),'PRIVATE':([0,18,37,],[7,7,7,]),'LBRACE':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[18,-30,18,-27,-28,18,18,18,18,-31,-32,-33,-34,-35,-36,-37,-38,-39,18,18,-30,18,-30,18,18,18,18,]),'LPAREN':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[19,-30,19,-27,-28,19,19,19,19,-31,-32,-33,-34,-35,-36,-37,-38,-39,19,19,-30,19,-30,19,19,19,19,]),'NUMBER_REAL':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[21,-30,21,-27,-28,21,21,21,21,-31,-32,-33,-34,-35,-36,-37,-38,-39,21,21,-30,21,-30,21,21,21,21,]),'NUMBER_HEX':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[22,-30,22,-27,-28,22,22,22,22,-31,-32,-33,-34,-35,-36,-37,-38,-39,22,22,-30,22,-30,22,22,22,22,]),'NUMBER_EXP':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[23,-30,23,-27,-28,23,23,23,23,-31,-32,-33,-34,-35,-36,-37,-38,-39,23,23,-30,23,-30,23,23,23,23,]),'NOT':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[24,-30,24,-27,-28,24,24,24,24,-31,-32,-33,-34,-35,-36,-37,-38,-39,24,24,-30,24,-30,24,24,24,24,]),'STRING_SINGLE':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[25,-30,25,-27,-28,25,25,25,25,-31,-32,-33,-34,-35,-36,-37,-38,-39,25,25,-30,25,-30,25,25,25,25,]),'STRING_DOUBLE':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[26,-30,26,-27,-28,26,26,26,26,-31,-32,-33,-34,-35,-36,-37,-38,-39,26,26,-30,26,-30,26,26,26,26,]),'LSPAREN':([0,8,9,11,12,18,19,24,27,28,29,30,31,32,33,34,35,36,37,38,39,41,44,52,56,60,62,],[27,-30,27,-27,-28,27,27,27,27,-31,-32,-33,-34,-35,-36,-37,-38,-39,27,27,-30,27,-30,27,27,27,27,]),'RBRACE':([2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,47,50,51,52,53,54,55,57,58,64,],[-1,-2,-5,-6,-7,-29,-22,-11,-27,-28,-12,-13,-14,-15,-16,-49,-19,-40,-41,-42,-49,-43,-44,-31,-32,-33,-34,-35,-36,-37,-38,-39,-49,-49,-30,-49,-24,-23,-29,54,-25,-3,-10,-49,-9,-17,-18,-21,-8,-20,]),'EQUAL':([8,11,12,40,],[41,-27,-28,52,]),'RPAREN':([9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,38,39,42,43,44,46,47,51,54,55,57,64,],[-22,-11,-27,-28,-12,-13,-14,-15,-16,-49,-19,-40,-41,-42,-49,-43,-44,-31,-32,-33,-34,-35,-36,-37,-38,-39,-49,-30,-24,-23,-29,55,-25,-10,-17,-18,-21,-20,]),'COMMA':([9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,42,43,44,47,48,49,51,54,55,56,57,59,60,61,64,],[-22,-11,-27,-28,-12,-13,-14,-15,-16,-19,-40,-41,-42,-49,-43,-44,-49,-31,-32,-33,-34,-35,-36,-37,-38,-39,-49,-30,-24,-23,-29,-25,56,-23,-10,-17,-18,-49,-21,60,-49,62,-20,]),'RSPAREN':([9,10,11,12,13,14,15,16,17,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,42,43,44,47,49,51,54,55,57,62,63,64,],[-22,-11,-27,-28,-12,-13,-14,-15,-16,-19,-40,-41,-42,-49,-43,-44,-49,-31,-32,-33,-34,-35,-36,-37,-38,-39,-49,-30,-24,-23,-29,-25,57,-10,-17,-18,-21,-49,64,-20,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,18,],[1,45,]),'statements':([0,18,],[2,2,]),'statement':([0,18,37,],[3,3,50,]),'empty':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[4,43,4,43,43,49,4,43,43,43,43,43,43,]),'assignment':([0,18,37,],[5,5,5,]),'binaryexpression':([0,18,19,27,37,38,41,52,56,60,62,],[6,6,46,48,6,51,53,58,59,61,63,]),'identifier':([0,6,7,9,18,19,24,27,37,38,41,46,48,51,52,53,56,58,59,60,61,62,63,],[8,39,40,44,8,44,44,44,8,44,44,39,39,39,44,39,44,39,39,44,39,44,39,]),'operator':([0,6,9,18,19,24,27,37,38,41,46,48,51,52,53,56,58,59,60,61,62,63,],[9,38,9,9,9,9,9,9,9,9,38,38,38,9,38,9,38,38,9,38,9,38,]),'primaryexpression':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[10,42,10,10,47,10,10,10,10,10,10,10,10,]),'number':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'unaryexpression':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[14,14,14,14,14,14,14,14,14,14,14,14,14,]),'nularexpression':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[15,15,15,15,15,15,15,15,15,15,15,15,15,]),'variable':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[16,16,16,16,16,16,16,16,16,16,16,16,16,]),'string':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[17,17,17,17,17,17,17,17,17,17,17,17,17,]),'array':([0,9,18,19,24,27,37,38,41,52,56,60,62,],[20,20,20,20,20,20,20,20,20,20,20,20,20,]),'punctuation':([0,6,9,18,19,24,27,37,38,41,46,48,51,52,53,56,58,59,60,61,62,63,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> statements','code',1,'p_code','sqf_yacc.py',21),
  ('code -> statement','code',1,'p_code','sqf_yacc.py',22),
  ('statements -> statement SEMI_COLON statement','statements',3,'p_statements','sqf_yacc.py',28),
  ('statements -> statement','statements',1,'p_statements','sqf_yacc.py',29),
  ('statement -> empty','statement',1,'p_statement','sqf_yacc.py',35),
  ('statement -> assignment','statement',1,'p_statement','sqf_yacc.py',36),
  ('statement -> binaryexpression','statement',1,'p_statement','sqf_yacc.py',37),
  ('assignment -> PRIVATE identifier EQUAL binaryexpression','assignment',4,'p_assignment','sqf_yacc.py',43),
  ('assignment -> identifier EQUAL binaryexpression','assignment',3,'p_assignment','sqf_yacc.py',44),
  ('binaryexpression -> binaryexpression operator binaryexpression','binaryexpression',3,'p_binaryexpression','sqf_yacc.py',50),
  ('binaryexpression -> primaryexpression','binaryexpression',1,'p_binaryexpression','sqf_yacc.py',51),
  ('primaryexpression -> number','primaryexpression',1,'p_primaryexpression','sqf_yacc.py',57),
  ('primaryexpression -> unaryexpression','primaryexpression',1,'p_primaryexpression','sqf_yacc.py',58),
  ('primaryexpression -> nularexpression','primaryexpression',1,'p_primaryexpression','sqf_yacc.py',59),
  ('primaryexpression -> variable','primaryexpression',1,'p_primaryexpression','sqf_yacc.py',60),
  ('primaryexpression -> string','primaryexpression',1,'p_primaryexpression','sqf_yacc.py',61),
  ('primaryexpression -> LBRACE code RBRACE','primaryexpression',3,'p_primaryexpression','sqf_yacc.py',62),
  ('primaryexpression -> LPAREN binaryexpression RPAREN','primaryexpression',3,'p_primaryexpression','sqf_yacc.py',63),
  ('primaryexpression -> array','primaryexpression',1,'p_primaryexpression','sqf_yacc.py',64),
  ('array -> LSPAREN binaryexpression COMMA binaryexpression COMMA binaryexpression COMMA binaryexpression RSPAREN','array',9,'p_array','sqf_yacc.py',70),
  ('array -> LSPAREN empty RSPAREN','array',3,'p_array','sqf_yacc.py',71),
  ('nularexpression -> operator','nularexpression',1,'p_nularexpression','sqf_yacc.py',77),
  ('nularexpression -> empty','nularexpression',1,'p_nularexpression','sqf_yacc.py',78),
  ('unaryexpression -> operator primaryexpression','unaryexpression',2,'p_unaryexpression','sqf_yacc.py',84),
  ('unaryexpression -> NOT primaryexpression','unaryexpression',2,'p_unaryexpression','sqf_yacc.py',85),
  ('unaryexpression -> empty','unaryexpression',1,'p_unaryexpression','sqf_yacc.py',86),
  ('identifier -> PRIVATE_ID','identifier',1,'p_identifier','sqf_yacc.py',92),
  ('identifier -> GLOBAL_ID','identifier',1,'p_identifier','sqf_yacc.py',93),
  ('variable -> identifier','variable',1,'p_variable','sqf_yacc.py',99),
  ('operator -> identifier','operator',1,'p_operator','sqf_yacc.py',105),
  ('operator -> punctuation','operator',1,'p_operator','sqf_yacc.py',106),
  ('punctuation -> DIVIDE','punctuation',1,'p_punctuation','sqf_yacc.py',112),
  ('punctuation -> MINUS','punctuation',1,'p_punctuation','sqf_yacc.py',113),
  ('punctuation -> MOD','punctuation',1,'p_punctuation','sqf_yacc.py',114),
  ('punctuation -> PLUS','punctuation',1,'p_punctuation','sqf_yacc.py',115),
  ('punctuation -> POW','punctuation',1,'p_punctuation','sqf_yacc.py',116),
  ('punctuation -> SELECT','punctuation',1,'p_punctuation','sqf_yacc.py',117),
  ('punctuation -> TIMES','punctuation',1,'p_punctuation','sqf_yacc.py',118),
  ('punctuation -> COLON','punctuation',1,'p_punctuation','sqf_yacc.py',119),
  ('number -> NUMBER_REAL','number',1,'p_number','sqf_yacc.py',125),
  ('number -> NUMBER_HEX','number',1,'p_number','sqf_yacc.py',126),
  ('number -> NUMBER_EXP','number',1,'p_number','sqf_yacc.py',127),
  ('string -> STRING_SINGLE','string',1,'p_string','sqf_yacc.py',133),
  ('string -> STRING_DOUBLE','string',1,'p_string','sqf_yacc.py',134),
  ('gte -> GT EQUAL','gte',2,'p_gte','sqf_yacc.py',140),
  ('lte -> LT EQUAL','lte',2,'p_lte','sqf_yacc.py',146),
  ('equality -> EQUAL EQUAL','equality',2,'p_equality','sqf_yacc.py',152),
  ('inequality -> NOT EQUAL','inequality',2,'p_inequality','sqf_yacc.py',158),
  ('empty -> <empty>','empty',0,'p_empty','sqf_yacc.py',164),
]
