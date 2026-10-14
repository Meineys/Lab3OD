def rpn_calculator(expression):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token in "+-*/":
            if stack.size() < 2:
                return "Некорректное выражение"
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(a / b)
        else:
            try:
                stack.push(float(token))
            except ValueError:
                return "Некорректное выражение"
    if stack.size() == 1:
        return stack.pop()
    return "Некорректное выражение"