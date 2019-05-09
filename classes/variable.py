class Variable:
    def __init__(self, name, lineno):
        self.name = name
        self.assigned = False
        self.uses = 0
        self.declared_at = lineno

    def set_assigned(self, state=True):
        self.assigned = state

    def increment_uses(self):
        self.uses += 1
