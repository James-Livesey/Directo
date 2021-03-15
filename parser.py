def parseExpression(expression):
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

    return tree