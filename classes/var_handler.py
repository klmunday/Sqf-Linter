from classes.variable import Variable


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

    def add_local_var(self, varname, lineno):
        self.get_current_frame()[varname.lower()] = Variable(varname.lower(), lineno)

    def update_local_var(self, varname):
        self.get_current_frame()[varname.lower()].set_assigned()

    def get_local_var(self, varname):
        for stack in reversed(self.local_var_stack):
            var = stack.get(varname)
            if var:
                var.increment_uses()
                return var
        return None

    def add_global_var(self, varname, lineno):
        self.global_vars.get(self.get_namespace())[varname.lower()] = Variable(varname.lower(), lineno)

    def update_global_var(self, varname):
        self.global_vars.get(self.get_namespace())[varname.lower()].set_assigned()

    def get_global_var(self, varname, namespace=''):
        namespace = self.get_namespace() if namespace == '' else namespace.lower()
        var = self.global_vars.get(namespace).get(varname.lower())
        if var:
            var.increment_uses()
            return var
        return None

    def new_local_scope(self):
        self.local_var_stack.append({})

    def pop_local_stack(self):
        unused_vars = {name: var for name, var in self.get_current_frame().items() if var.uses == 0}
        self.local_var_stack.pop()
        return unused_vars

    def change_namespace(self, namespace):
        self.cur_namespace.append(namespace.lower())

    def pop_namespace(self):
        self.cur_namespace.pop()

    def get_namespace(self):
        return self.cur_namespace[-1]

    def has_local_var(self, varname):
        for stack in reversed(self.local_var_stack):
            if stack.get(varname.lower()) is not None:
                return True
        return False

    def has_global_var(self, varname):
        return self.global_vars.get(self.get_namespace()).get(varname.lower()) is not None
