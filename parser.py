from typing import List

import types
import commands

class ValueCandidate:
    def __init__(self, data: str = ""):
        self.data = data

    def resolve(self):
        if self.data == "0" or self.data == "1":
            return types.Bit(self.data == "1")

        return types.Input(self.data)

class Statement:
    def __init__(self, command: commands.Command, parameters: List[types.Value]):
        self.command = command
        self.parameters = parameters

def parseExpression(expression: str):
    tree = []
    bracketStart = 0
    bracketDepth = 0

    for i in range(0, len(expression)):
        if expression[i] == "(":
            if bracketDepth == 0: bracketStart = i

            bracketDepth += 1
        elif expression[i] == ")":
            bracketDepth -= 1

            if bracketDepth == 0:
                tree.append(parseExpression(expression[bracketStart + 1:i]))
        elif bracketDepth == 0: tree.append(expression[i])

    tokens = [ValueCandidate]
    inString = False

    for symbol in tree[1:]:
        if symbol == " " and not inString:
            tokens.append(ValueCandidate())
        elif isinstance(symbol, Statement) and not inString:
            tokens[-1] = symbol
        elif symbol == "\"":
            if not inString:
                tokens[-1] = types.String

            inString = not inString
        else:
            if isinstance(tokens[-1], types.String):
                tokens[-1].data += symbol
            elif isinstance(tokens[-1], ValueCandidate):
                tokens[-1].data += symbol
            else:
                tokens[-1] = ValueCandidate(symbol)

    parameters = []

    for token in tokens:
        if isinstance(token, ValueCandidate):
            parameters.append(token.resolve())
        else:
            parameters.append(token)

    return Statement(tree[0], parameters)

a = parseExpression("& 1 (| 0 1)")