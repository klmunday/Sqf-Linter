import pprint


class VarHandler:
    def __init__(self):
        self.local_var_stack = []
        self.global_vars = {
            'missionNamespace': {},
            'parsingNamespace': {},
            'profileNamespace': {},
            'uiNamespace': {},
        }
        self.cur_namespace = 'missionNamespace'
        self.cur_local_stack = {}

    def add_local_var(self, varname, value='ANY'):
        self.cur_local_stack[varname.lower()] = value
        pprint.pprint(self.cur_local_stack, indent=4)

    def get_local_var(self, varname):
        if self.cur_local_stack.get(varname):
            return True
        for stack in reversed(self.local_var_stack):
            value = stack.get(varname)
            if value:
                return value
        return None

    def add_global_var(self, varname, value='ANY'):
        self.global_vars.get(self.cur_namespace)[varname.lower()] = value
        pprint.pprint(self.global_vars, indent=4)

    def get_global_var(self, varname, namespace=''):
        namespace = self.cur_namespace if namespace == '' else namespace
        return self.global_vars.get(namespace).get(varname)

    def new_local_scope(self):
        self.local_var_stack.append(self.cur_local_stack)
        self.cur_local_stack.clear()

    def pop_local_stack(self):
        self.local_var_stack.pop()

    def change_namespace(self, namespace):
        self.cur_namespace = namespace

    def has_local_var(self, varname):
        if self.cur_local_stack.get(varname):
            return True
        for stack in self.local_var_stack:
            if stack.get(varname.lower()):
                return True
        return False

    def has_global_var(self, varname, namespace=''):
        namespace = self.cur_namespace if namespace == '' else namespace
        return self.global_vars.get(namespace).get(varname.lower())

    def has_any_var(self, varname):
        varname = varname.lower()
        return any([self.has_local_var(varname), self.has_global_var(varname, self.cur_namespace)])
