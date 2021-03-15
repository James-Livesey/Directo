import types

class Command:
    def __init__(self):
        pass

class AND(Command):
    def __init__(self, *inputs):
        self.inputs = inputs

    def generateRules(self):
        for input in self.inputs:
            if isinstance(input, types.Bit) and input.data == False:
                return types.Rule([]) # We know that this gate is not reversible when one of the inputs is going to be 0

        return types.Rule([types.Permutation(types.Bit(True))] * len(self.inputs))