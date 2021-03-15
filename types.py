class Value:
    def __init__(self):
        self.data = None

class Input(Value):
    def __init__(self, data: str):
        self.data = data

class String(Value):
    def __init__(self, data: str = ""):
        self.data = data

class Bit(Value):
    def __init__(self, data: bool = False):
        self.data = data

class Permutation:
    def __init__(self, expectedValues):
        self.expectedValues = expectedValues

class Rule:
    def __init__(self, permutations):
        self.permutations = permutations

class Rules(Value):
    def __init__(self, data):
        self.data = data