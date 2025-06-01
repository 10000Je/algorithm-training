import sys

def isBalanced(string):
    stack = []
    for char in string:
        if char in ['(', '[']:
            stack.append(char)
        elif char in [')', ']']:
            if len(stack) == 0:
                return False
            else:
                last_char = stack.pop()
                if (char == ')' and last_char != '(') or (char == ']' and last_char != '['):
                    return False
        else:
            pass
    return not stack
                    

str1 = sys.stdin.readline().rstrip()
while str1 != '.':
    print('yes' if isBalanced(str1) else 'no')
    str1 = sys.stdin.readline().rstrip()