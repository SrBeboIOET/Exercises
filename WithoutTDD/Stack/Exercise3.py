string = input("Enter the string: ")
reverse=string
stack = []

def reverse_string(string):
    result_string=""

    for character in string:
        stack.append(character)

    while stack:
        result_string += stack.pop()

    return result_string

print("\nThe reverse of: ", string, "is: \n", reverse_string(reverse))
