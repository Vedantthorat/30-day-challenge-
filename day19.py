def evaluate_postfix(expression: str) -> int:
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.lstrip('-').isdigit():  # check for integers (including negative)
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # truncating toward zero
    
    return stack[0]
