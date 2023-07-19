string = input("Enter the postfix expression with a space of separation: ")
postfix=string
stack = []

def calculate_result(string):
    characters = {'+': '+', '-': '-', '*': '*', '/': '/'}
    tokens = string.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        if token in characters:
            operator2 = stack.pop()
            operator1 = stack.pop()
            result = None
            if token == '+':
                result = operator1 + operator2
            if token == '-':
                result = operator1 - operator2
            if token == '*':
                result = operator1 * operator2
            if token == '/':
                result = operator1 / operator2
            if token == '%':
                result = operator1 % operator2
            stack.append(result)
        
    return stack.pop()

print("The result of: ", postfix, "is: ", calculate_result(postfix))
