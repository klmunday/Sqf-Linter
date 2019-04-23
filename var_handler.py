class VarHandler:
    def __init__(self):
        self.global_vars = {
            'missionnamespace': {},
            'parsingnamespace': {},
            'profilenamespace': {},
            'uinamespace': {},
        }
        self.cur_namespace = ['missionnamespace']
        self.local_var_stack = [{}]

    def __str__(self):
        return f'\nglobal_vars: {self.global_vars}' \
               f'\ncur_namespace: {self.cur_namespace}' \
               f'\nlocal_var_stack: {self.local_var_stack}'

    def get_current_frame(self):
        return self.local_var_stack[-1]

    def add_local_var(self, varname, value='ANY'):
        print(f'ADDING NEW LOCAL VARIABLE: {varname} = {value}')
        self.get_current_frame()[varname.lower()] = value
        print(f'UPDATED VAR_HANDLER:{self}')

    def get_local_var(self, varname):
        for stack in reversed(self.local_var_stack):
            value = stack.get(varname)
            if value is not None:
                return value
        return None

    def add_global_var(self, varname, value='ANY'):
        self.global_vars.get(self.get_namespace())[varname.lower()] = value

    def get_global_var(self, varname, namespace=''):
        namespace = self.cur_namespace if namespace == '' else namespace.lower()
        return self.global_vars.get(namespace).get(varname.lower())

    def new_local_scope(self):
        print(f'CREATING NEW LOCAL SCOPE')
        self.local_var_stack.append({})
        print(f'UPDATED VAR_HANDLER:{self}')

    def pop_local_stack(self):
        print(f'POPPING LOCAL SCOPE')
        self.local_var_stack.pop()
        print(f'UPDATED VAR_HANDLER:{self}')

    def change_namespace(self, namespace):
        self.cur_namespace.append(namespace)

    def pop_namespace(self):
        self.cur_namespace.pop()

    def get_namespace(self):
        return self.cur_namespace[-1]

    def has_local_var(self, varname):
        for stack in reversed(self.local_var_stack):
            if stack.get(varname.lower()) is not None:
                return True
        return False

    def has_global_var(self, varname, namespace=''):
        namespace = self.cur_namespace if namespace == '' else namespace.lower()
        return self.global_vars.get(namespace).get(varname.lower()) is not None

    def has_any_var(self, varname):
        varname = varname.lower()
        return any([self.has_local_var(varname), self.has_global_var(varname, self.get_namespace())])
