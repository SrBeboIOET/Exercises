string = input("Enter a string of characteres: ")
flag = True

def is_balance_string(string):
    stack = []
    balances  = {'(': ')', '[': ']', '{': '}'}

    for special_character in string: 
        if special_character in balances.keys(): 
            stack.append(special_character) 
        if special_character in balances.values(): 
            if not stack or balances[stack.pop()] != special_character: 
                return False
            
    return len(stack) == 0

if is_balance_string(string):
    print("There is a balance")
    
if not is_balance_string(string):
    print("There is not a balance")
