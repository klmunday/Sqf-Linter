
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEMODleftPOWrightUMINUSAND BOOL COLON COMMA COMMENT_MULTI COMMENT_SINGLE DIVIDE ELSE EQUAL FOR GLOBAL_ID GT IF LBRACE LPAREN LSPAREN LT MINUS MOD NEWLINE NOT NUMBER_EXP NUMBER_HEX NUMBER_REAL OR PLUS POW PRIVATE PRIVATE_ID RBRACE RPAREN RSPAREN SELECT SEMI_COLON STRING_DOUBLE STRING_SINGLE SWITCH TIMES WHILE WITH\n    expressions : expression SEMI_COLON expressions\n                | expression SEMI_COLON\n    \n    expression  : LPAREN expression RPAREN\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression TIMES expression\n                | expression DIVIDE expression\n                | expression MOD expression\n                | expression POW expression\n                | assignment\n                | number\n                | identifier\n    \n    expression : MINUS expression %prec UMINUS\n    \n    assignment  : PRIVATE PRIVATE_ID EQUAL expression\n                | GLOBAL_ID EQUAL expression\n    \n    identifier  : PRIVATE_ID\n                | GLOBAL_ID\n    \n    number  : NUMBER_REAL\n            | NUMBER_HEX\n            | NUMBER_EXP\n    \n    empty :\n    '
    
_lr_action_items = {'LPAREN':([0,3,4,14,15,16,17,18,19,20,24,33,],[3,3,3,3,3,3,3,3,3,3,3,3,]),'MINUS':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,26,27,28,29,30,31,32,33,34,35,],[4,16,4,4,-10,-11,-12,-16,-17,-18,-19,-20,4,4,4,4,4,4,4,16,-13,4,-4,-5,-6,-7,-8,-9,-3,4,16,16,]),'PRIVATE':([0,3,4,14,15,16,17,18,19,20,24,33,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'GLOBAL_ID':([0,3,4,14,15,16,17,18,19,20,24,33,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'NUMBER_REAL':([0,3,4,14,15,16,17,18,19,20,24,33,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'NUMBER_HEX':([0,3,4,14,15,16,17,18,19,20,24,33,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'NUMBER_EXP':([0,3,4,14,15,16,17,18,19,20,24,33,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'PRIVATE_ID':([0,3,4,8,14,15,16,17,18,19,20,24,33,],[9,9,9,23,9,9,9,9,9,9,9,9,9,]),'$end':([1,14,25,],[0,-2,-1,]),'SEMI_COLON':([2,5,6,7,9,10,11,12,13,22,26,27,28,29,30,31,32,34,35,],[14,-10,-11,-12,-16,-17,-18,-19,-20,-13,-4,-5,-6,-7,-8,-9,-3,-15,-14,]),'PLUS':([2,5,6,7,9,10,11,12,13,21,22,26,27,28,29,30,31,32,34,35,],[15,-10,-11,-12,-16,-17,-18,-19,-20,15,-13,-4,-5,-6,-7,-8,-9,-3,15,15,]),'TIMES':([2,5,6,7,9,10,11,12,13,21,22,26,27,28,29,30,31,32,34,35,],[17,-10,-11,-12,-16,-17,-18,-19,-20,17,-13,17,17,-6,-7,-8,-9,-3,17,17,]),'DIVIDE':([2,5,6,7,9,10,11,12,13,21,22,26,27,28,29,30,31,32,34,35,],[18,-10,-11,-12,-16,-17,-18,-19,-20,18,-13,18,18,-6,-7,-8,-9,-3,18,18,]),'MOD':([2,5,6,7,9,10,11,12,13,21,22,26,27,28,29,30,31,32,34,35,],[19,-10,-11,-12,-16,-17,-18,-19,-20,19,-13,19,19,-6,-7,-8,-9,-3,19,19,]),'POW':([2,5,6,7,9,10,11,12,13,21,22,26,27,28,29,30,31,32,34,35,],[20,-10,-11,-12,-16,-17,-18,-19,-20,20,-13,20,20,20,20,20,-9,-3,20,20,]),'RPAREN':([5,6,7,9,10,11,12,13,21,22,26,27,28,29,30,31,32,34,35,],[-10,-11,-12,-16,-17,-18,-19,-20,32,-13,-4,-5,-6,-7,-8,-9,-3,-15,-14,]),'EQUAL':([10,23,],[24,33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressions':([0,14,],[1,25,]),'expression':([0,3,4,14,15,16,17,18,19,20,24,33,],[2,21,22,2,26,27,28,29,30,31,34,35,]),'assignment':([0,3,4,14,15,16,17,18,19,20,24,33,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'number':([0,3,4,14,15,16,17,18,19,20,24,33,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'identifier':([0,3,4,14,15,16,17,18,19,20,24,33,],[7,7,7,7,7,7,7,7,7,7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expressions","S'",1,None,None,None),
  ('expressions -> expression SEMI_COLON expressions','expressions',3,'p_expressions','sqf_yacc.py',18),
  ('expressions -> expression SEMI_COLON','expressions',2,'p_expressions','sqf_yacc.py',19),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','sqf_yacc.py',26),
  ('expression -> expression PLUS expression','expression',3,'p_expression','sqf_yacc.py',27),
  ('expression -> expression MINUS expression','expression',3,'p_expression','sqf_yacc.py',28),
  ('expression -> expression TIMES expression','expression',3,'p_expression','sqf_yacc.py',29),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','sqf_yacc.py',30),
  ('expression -> expression MOD expression','expression',3,'p_expression','sqf_yacc.py',31),
  ('expression -> expression POW expression','expression',3,'p_expression','sqf_yacc.py',32),
  ('expression -> assignment','expression',1,'p_expression','sqf_yacc.py',33),
  ('expression -> number','expression',1,'p_expression','sqf_yacc.py',34),
  ('expression -> identifier','expression',1,'p_expression','sqf_yacc.py',35),
  ('expression -> MINUS expression','expression',2,'p_expr_uminus','sqf_yacc.py',43),
  ('assignment -> PRIVATE PRIVATE_ID EQUAL expression','assignment',4,'p_assignment','sqf_yacc.py',51),
  ('assignment -> GLOBAL_ID EQUAL expression','assignment',3,'p_assignment','sqf_yacc.py',52),
  ('identifier -> PRIVATE_ID','identifier',1,'p_identifier','sqf_yacc.py',60),
  ('identifier -> GLOBAL_ID','identifier',1,'p_identifier','sqf_yacc.py',61),
  ('number -> NUMBER_REAL','number',1,'p_number','sqf_yacc.py',69),
  ('number -> NUMBER_HEX','number',1,'p_number','sqf_yacc.py',70),
  ('number -> NUMBER_EXP','number',1,'p_number','sqf_yacc.py',71),
  ('empty -> <empty>','empty',0,'p_empty','sqf_yacc.py',79),
]
