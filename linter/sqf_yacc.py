import ply.yacc as pyacc
from classes.namespace import Namespace
import sys
from linter.sqf_lex import tokens, unary_functions, binary_functions, nular_functions
from linter.sqf_linter import global_var_handler
from classes.var_handler import VarHandler

var_handler = VarHandler()

terminators = {
    ';': 0,
    ',': 0,
}
is_interpreting = True  # This indicates whether the parser should pass the code as if it was being executed

literals = []

engine_functions = unary_functions + binary_functions + nular_functions

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'COMPARISON_OP', 'CONFIG_ACCESSOR_GTGT'),
    ('left', 'BINARY_OP', 'COLON'),
    ('left', 'ELSE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD', 'CONFIG_ACCESSOR_SLASH'),
    ('left', 'POW'),
    ('left', 'UNARY_OP'),
    ('left', 'NULAR_OP', 'VARIABLE', 'VALUE', 'BRACED_EXP'),
)


def p_code(p):
    """
    code    : empty
            | statement
            | statement terminator code
    """
    p[0] = p[len(p) - 1]


def p_statement(p):
    """
    statement   : controlstructure
                | assignment
                | binaryexp
                | nularexp
                | unaryexp
                | primaryexp
    """
    p[0] = p[1]


def p_terminator(p):
    """
    terminator  : SEMI_COLON
                | COMMA
    """
    terminators[p[1]] += 1
    if all(terminators.values()):
        semi_count = terminators.get(';')
        comma_count = terminators.get(',')
        if p[1] is not ';':
            print(f'WARNING: File contains mixed line terminators. "{p[1]}" seen on line: {p.lineno(1)}. '
                  f'Current count: (; {semi_count}), (, {comma_count}). '
                  f'Recommended to use ; as it is standard.')


def p_controlstructure(p):
    """
    controlstructure    : ifstatement
                        | whileloop
                        | forloop
                        | withstatement
                        | foreachloop
                        | switchstatement
    """
    p[0] = p[1]


def p_helpertype(p):
    """
    helpertype  : iftype
                | whiletype
                | fortype
                | withtype
    """
    p[0] = p[1]


def p_case(p):
    """
    case    : CASE primaryexp COLON bracedexp
            | CASE primaryexp
            | DEFAULT bracedexp
    """


def p_switchstatement(p):
    """
    switchstatement : SWITCH LPAREN primaryexp RPAREN DO LBRACE switchbody RBRACE
    """


def p_switchbody(p):
    """
    switchbody  : empty
                | case
                | case terminator switchbody
    """


def p_iftype(p):
    """
    iftype  : IF bracedexp_condition
            | IF LPAREN primaryexp RPAREN
    """
    p[0] = p[1]


def p_ifstatement(p):
    """
    ifstatement : iftype THEN bracedexp ELSE bracedexp
                | iftype THEN bracedexp
                | iftype EXITWITH bracedexp
    """
    p[0] = p[1]
    

def p_withtype(p):
    """
    withtype : WITH NAMESPACE
    """
    p[0] = Namespace(p[2])


def p_withstatementinit(p):
    """
    withstatementinit : withtype DO
    """
    if isinstance(p[1], Namespace):
        var_handler.change_namespace(p[1].value)
    else:
        print(f'WARNING: Possible error with WithType used on line: {p.lineno(1)}.')


def p_withstatement(p):
    """
    withstatement : withstatementinit bracedexp
    """
    p[0] = p[2]


def p_whiletype(p):
    """
    whiletype   : WHILE bracedexp_condition
    """


def p_whileloop(p):
    """
    whileloop : whiletype DO bracedexp
    """
    p[0] = p[3]


def p_foreachloop(p):
    """
    foreachloop : bracedexp FOREACH array
                | bracedexp FOREACH primaryexp
                | bracedexp FOREACH LPAREN primaryexp RPAREN
    """


def p_fortype(p):
    """
    fortype : FOR new_scope string FROM primaryexp TO primaryexp
            | FOR new_scope string FROM primaryexp TO primaryexp STEP primaryexp
            | FOR new_scope LSPAREN bracedexp_noscope COMMA bracedexp_condition COMMA bracedexp_noscope RSPAREN
    """
    if p[3] != '[':
        if p[3][0] in ["'", '"']:
            p[3] = p[3].replace('"', '')
            p[3] = p[3].replace("'", "")
        if p[3][0] is '_':
            if var_handler.has_local_var(p[3]):
                if get_interpretation_state:
                    print(f'ERROR: Local variable {p[3]} already defined. Occurs on line: {p.lineno(1)}.')
                p[0] = p[3]
            else:
                if not p[3][1].islower():
                    print(f'WARNING: Local variable {p[3]} defined with unconventional casing. on line: {p.lineno(1)}. '
                          f'Use lower case for the first character of local variables.')
                var_handler.add_local_var(p[3], p.lineno(1))
        else:
            var_handler.add_global_var(p[3], p.lineno(1))


def p_forloop(p):
    """
    forloop : fortype DO bracedexp_noscope
    """
    pop_vars_and_warning_unused()
    p[0] = p[3]
    

def p_bracedexp_condition(p):
    """
    bracedexp_condition   : LBRACE booleanexp RBRACE
                        | identifier
    """
    if len(p) is 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_bracedexp_noscope(p):
    """
     bracedexp_noscope : LBRACE code RBRACE
    """
    p[0] = p[2]


def p_getvariable_ns(p):
    """
    getvariable_ns  : NAMESPACE GETVARIABLE string
                    | NAMESPACE GETVARIABLE LSPAREN string COMMA primaryexp RSPAREN
    """
    if len(p) == 4:
        p[3] = p[3].replace("'", "")
        p[3] = p[3].replace('"', '')
        if not var_handler.get_global_var(p[3], p[1]):
            print(f'ERROR: getVariable failed on line {p.lineno(2)}. {p[3]} not found in namespace: {p[1]}. '
                  f'Check if it is undefined or in a different namespace.')
        else:
            p[0] = var_handler.get_global_var(p[3], p[1])
    elif len(p) == 8:
        p[4] = p[4].replace("'", "")
        p[4] = p[4].replace('"', '')
        if not var_handler.get_global_var(p[4], p[1]):
            print(f'ERROR: getVariable failed on line {p.lineno(2)}. {p[4]} not found in namespace: {p[1]}. '
                  f'Check if it is undefined or in a different namespace.'
                  f'Defaulting to default value: {p[6]}')
        else:
            p[0] = var_handler.get_global_var(p[4], p[1])


def p_getvariable_any(p):
    """
    getvariable_any : primaryexp GETVARIABLE string
                    | primaryexp GETVARIABLE LSPAREN string COMMA primaryexp RSPAREN
    """
    print(f'WARNING: getVariable called on a non-namespace object on line: {p.lineno(2)}. '
          f'Cannot guaranty success, recommend manual check.')


def p_setvariable_ns(p):
    """
    setvariable_ns  : NAMESPACE SETVARIABLE LSPAREN string COMMA primaryexp RSPAREN
                    | NAMESPACE SETVARIABLE LSPAREN string COMMA primaryexp COMMA booleanexp RSPAREN
    """
    p[4] = p[4].replace('"', '')
    p[4] = p[4].replace("'", "")
    var_handler.add_global_var(p[4], p.lineno(2), p[1])


def p_setvariable_any(p):
    """
    setvariable_any     : primaryexp SETVARIABLE LSPAREN string COMMA primaryexp RSPAREN
                        | primaryexp SETVARIABLE LSPAREN string COMMA primaryexp COMMA booleanexp RSPAREN
    """
    print(f'WARNING: setVariable called on a non-namespace object on line: {p.lineno(2)}. '
          f'Cannot guaranty success, recommend manual check.')


def p_param_unary(p):
    """
    param_unary     : PARAM LSPAREN number RSPAREN
                    | PARAM LSPAREN number COMMA primaryexp RSPAREN
                    | PARAM LSPAREN number COMMA primaryexp COMMA array RSPAREN
                    | PARAM LSPAREN number COMMA primaryexp COMMA array COMMA number RSPAREN
                    | PARAM LSPAREN number COMMA primaryexp COMMA array COMMA array RSPAREN
    """
    if len(p) != 5:
        p[0] = p[5]
    print(f'WARNING: Unable to check value passing into param on line: {p.lineno(2)}. '
          f'Please check manually.')


def p_param_binary(p):
    """
    param_binary    : primaryexp PARAM LSPAREN number RSPAREN
                    | primaryexp PARAM LSPAREN number COMMA primaryexp RSPAREN
                    | primaryexp PARAM LSPAREN number COMMA primaryexp COMMA array RSPAREN
                    | primaryexp PARAM LSPAREN number COMMA primaryexp COMMA array COMMA number RSPAREN
                    | primaryexp PARAM LSPAREN number COMMA primaryexp COMMA array COMMA array RSPAREN
    """
    if len(p) != 6:
        p[0] = p[6]
    print(f'WARNING: Unable to check value passing into param on line: {p.lineno(2)}. '
          f'Please check manually.')


def p_params_unary(p):
    """
    params_unary : PARAMS params_array
    """


def p_params_binary(p):
    """
    params_binary : primaryexp PARAMS params_array
    """


def p_params_array(p):
    """
    params_array    : LSPAREN RSPAREN
                    | LSPAREN params_element RSPAREN
    """
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


def p_params_array_element(p):
    """
    params_element  : params_array_entry
                    | params_array_entry COMMA params_element
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if isinstance(p[3], list):
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]] + [p[3]]


def p_params_array_entry(p):
    """
    params_array_entry  : string
                        | LSPAREN string COMMA primaryexp RSPAREN
                        | LSPAREN string COMMA primaryexp COMMA array RSPAREN
                        | LSPAREN string COMMA primaryexp COMMA array COMMA number RSPAREN
                        | LSPAREN string COMMA primaryexp COMMA array COMMA array RSPAREN
    """
    var = p[1] if len(p) == 2 else p[2]
    var = var.replace("'", "")
    var = var.replace('"', '')
    if var_handler.get_local_var(var):
        print(f'ERROR: Local variable {var} already defined. Occurs on line: {p.lineno(1)}.')
        return
    if not var.startswith('_') and var is not "":
        print(f'ERROR: Variable must be begin with an _ in params entry on line: {p.lineno(1)}')
    else:
        if var is not "":
            if not var[1].islower():
                print(f'WARNING: Local variable {var} defined with unconventional casing. on line: {p.lineno(1)}. '
                      f'Use lower case for the first character of local variables.')
            var_handler.add_local_var(var, p.lineno(1))


def p_vardefinition(p):
    """
    vardefinition   : definition
                    | arraydefinition
    """


def p_assignment(p):
    """
    assignment  : assignment_code code RBRACE
                | definition EQUAL primaryexp
                | variable EQUAL primaryexp
    """
    if p[1] in engine_functions:
        print(f'ERROR: Engine function assignment attempted on line: {p.lineno(1)}. '
              f'Engine functions cannot be assigned to.')
    elif not p[1].startswith('_'):
        var_handler.add_global_var(p[1], p.lineno(1))
    elif not var_handler.has_local_var(p[1]):
        var_handler.add_local_var(p[1], p.lineno(2))
    elif not p[1].startswith('_'):
        var_handler.add_global_var(p[1], p.lineno(1))
    if not get_interpretation_state():
        set_interpretation_state(True)


def p_assignment_code(p):
    """
    assignment_code : definition EQUAL LBRACE
                    | variable EQUAL LBRACE
    """
    #  Make parser read the braced code without "simulating" execution
    set_interpretation_state(False)
    p[0] = p[1]


def p_arraydefinition(p):
    """
    arraydefinition : PRIVATE stringarray
    """
    for index, element in enumerate(p[2]):
        element = element.replace('"', '')
        element = element.replace("'", "")
        if var_handler.has_local_var(element):
            print(f'ERROR: Local variable {element} already defined. Occurs on line: {p.lineno(1)}.')
        else:
            if element[0] is not '_':
                print(f'ERROR: Attempt to declare global variable {element} as private on line: {p.lineno(1)}.')
            if not element[1].islower():
                print(f'WARNING: Local variable {element} defined with unconventional casing on line: {p.lineno(1)}. '
                      f'Use lower case for the first character of local variables.')
            var_handler.add_local_var(element, p.lineno(1))


def p_definition(p):
    """
    definition  : PRIVATE PRIVATE_ID
                | PRIVATE string
    """
    if p[2][0] in ['"', "'"]:
        p[2] = p[2].replace('"', '')
        p[2] = p[2].replace("'", "")
    if var_handler.has_local_var(p[2]):
        if get_interpretation_state:
            print(f'ERROR: Local variable {p[2]} already defined. Occurs on line: {p.lineno(1)}.')
        p[0] = p[2]
    else:
        if not p[2][1].islower():
            print(f'WARNING: Local variable {p[2]} defined with unconventional casing. on line: {p.lineno(1)}. '
                  f'Use lower case for the first character of local variables.')
        var_handler.add_local_var(p[2], p.lineno(1))
        p[0] = p[2]


def p_identifier(p):
    """
    identifier  : PRIVATE_ID %prec VARIABLE
                | GLOBAL_ID  %prec VARIABLE
    """
    if p[1].lower() in engine_functions:
        p[0] = p[1].lower()
    elif var_handler.has_local_var(p[1]):
        p[0] = var_handler.get_local_var(p[1])
    elif not p[1].startswith('_'):
        if var_handler.has_global_var(p[1]):
            p[0] = var_handler.get_global_var(p[1])
        else:
            print(f'WARNING: Possible undeclared global variable {p[1]} on line {p.lineno(1)}. '
                  f'Please check manually, it may just be a function that I can\'t read')
            var_handler.add_global_var(p[1], p.lineno(1))
            p[0] = p[1]
    else:
        if get_interpretation_state():
            print(f'ERROR: Undefined local variable {p[1]} used on line {p.lineno(1)}.')
        p[0] = p[1]


def p_variable(p):
    """
    variable    : PRIVATE_ID %prec VARIABLE
                | GLOBAL_ID %prec VARIABLE
    """
    p[0] = p[1]


def p_binaryexp(p):
    """
    binaryexp   : primaryexp BINARY_FNC primaryexp          %prec BINARY_OP
                | primaryexp comparisonoperator primaryexp  %prec BINARY_OP
                | primaryexp mathoperator primaryexp        %prec BINARY_OP
                | getvariable_ns                            %prec BINARY_OP
                | getvariable_any                           %prec BINARY_OP
                | setvariable_ns                            %prec BINARY_OP
                | setvariable_any                           %prec BINARY_OP
                | param_binary                              %prec BINARY_OP
                | params_binary                             %prec BINARY_OP
    """


def p_primaryexp(p):
    """
    primaryexp  : number                    %prec VALUE
                | identifier                %prec VALUE
                | controlstructure
                | helpertype
                | array                     %prec VALUE
                | unaryexp                  %prec UNARY_OP
                | nularexp                  %prec NULAR_OP
                | string                    %prec VALUE
                | binaryexp                 %prec BINARY_OP
                | bracedexp                 %prec BRACED_EXP
                | LPAREN primaryexp RPAREN  %prec VALUE
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_bracedexp(p):
    """
    bracedexp   : LBRACE new_scope code RBRACE
                | LBRACE RBRACE
    """
    if len(p) == 5:
        p[0] = p[3]
        pop_vars_and_warning_unused()


def p_new_scope(p):
    """new_scope :"""
    var_handler.new_local_scope()


def p_array(p):
    """
    array   : LSPAREN RSPAREN
            | LSPAREN arrayelement RSPAREN
    """
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


def p_arrayelement(p):
    """
    arrayelement    : primaryexp
                    | primaryexp COMMA arrayelement
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if isinstance(p[3], list):
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]] + [p[3]]


def p_stringarray(p):
    """
    stringarray : LSPAREN RSPAREN
                | LSPAREN stringarrayelement RSPAREN
    """
    if len(p) == 3:
        p[0] = []
    else:
        p[0] = p[2]


def p_stringarrayelement(p):
    """
    stringarrayelement  : string
                        | string COMMA stringarrayelement
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        if isinstance(p[3], list):
            p[0] = [p[1]] + p[3]
        else:
            p[0] = [p[1]] + [p[3]]


def p_nularexp(p):
    """
    nularexp    : NULAR_FNC     %prec NULAR_OP
                | identifier    %prec NULAR_OP
    """
    p[0] = p[1]
    

def p_unaryexp(p):
    """
    unaryexp    : UNARY_FNC primaryexp  %prec UNARY_OP
                | PLUS primaryexp       %prec UNARY_OP
                | MINUS primaryexp      %prec UNARY_OP
                | NOT primaryexp        %prec UNARY_OP
                | vardefinition         %prec UNARY_OP
                | param_unary           %prec UNARY_OP
                | params_unary          %prec UNARY_OP
    """


def p_comparisonoperator(p):
    """
    comparisonoperator  : LT            %prec COMPARISON_OP
                        | GT            %prec COMPARISON_OP
                        | LTE           %prec COMPARISON_OP
                        | GTE           %prec COMPARISON_OP
                        | EQUALITY      %prec COMPARISON_OP
                        | INEQUALITY    %prec COMPARISON_OP
                        | AND           %prec COMPARISON_OP
                        | OR            %prec COMPARISON_OP
    """
    p[0] = p[1]


def p_mathoperator(p):
    """
    mathoperator : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD
                    | POW
    """
    p[0] = p[1]


def p_booleanexp(p):
    """
    booleanexp  : primaryexp
                | primaryexp comparisonoperator booleanexp
                | primaryexp comparisonoperator LBRACE booleanexp RBRACE
    """


def p_configaccessor(p):
    """
    configaccessor  : GT GT     %prec CONFIG_ACCESSOR_GTGT
                    | DIVIDE    %prec CONFIG_ACCESSOR_SLASH
    """
    p[0] = ''.join(p[1:])


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
        print('ERROR: Unexpected "{}" on line:{}, pos:{}\n'.format(p.value, p.lineno, p.lexpos))
    else:
        print('ERROR: File possibly contains an incomplete statement.\n')


def get_interpretation_state():
    global is_interpreting
    return is_interpreting


def set_interpretation_state(state):
    global is_interpreting
    is_interpreting = state


def pop_vars_and_warning_unused():
    unused = var_handler.pop_local_stack()
    for name, var in unused.items():
        print(f'WARNING: Unused variable {name} declared on line: {var.declared_at}.')


parser = pyacc.yacc()


def yacc():
    return parser
