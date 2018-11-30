class VarHandler:
    def __init__(self):
        self.global_vars = {
            'missionnamespace': {},
            'parsingnamespace': {},
            'profilenamespace': {},
            'uinamespace': {},
        }
        self.cur_namespace = 'missionnamespace'
        self.local_var_stack = [{}]

    def __str__(self):
        return f'\nVARIABLE HANDLER' \
               f'\nglobal_vars: {self.global_vars}' \
               f'\ncur_namespace: {self.cur_namespace}' \
               f'\nlocal_var_stack: {self.local_var_stack}' \
               f'\n\n'

    def get_current_frame(self):
        return self.local_var_stack[-1]

    def add_local_var(self, varname, value='ANY'):
        self.get_current_frame()[varname.lower()] = value

    def get_local_var(self, varname):
        for stack in reversed(self.local_var_stack):
            value = stack.get(varname)
            if value:
                return value
        return None

    def add_global_var(self, varname, value='ANY'):
        self.global_vars.get(self.cur_namespace)[varname.lower()] = value

    def get_global_var(self, varname, namespace=''):
        namespace = self.cur_namespace if namespace == '' else namespace.lower()
        return self.global_vars.get(namespace).get(varname)

    def new_local_scope(self):
        self.local_var_stack.append({})

    def pop_local_stack(self):
        self.local_var_stack.pop()

    def change_namespace(self, namespace):
        self.cur_namespace = namespace.lower()

    def has_local_var(self, varname):
        for stack in reversed(self.local_var_stack):
            if stack.get(varname.lower()):
                return True
        return False

    def has_global_var(self, varname, namespace=''):
        namespace = self.cur_namespace if namespace == '' else namespace.lower()
        return self.global_vars.get(namespace).get(varname.lower())

    def has_any_var(self, varname):
        varname = varname.lower()
        return any([self.has_local_var(varname), self.has_global_var(varname, self.cur_namespace)])
