import sys

def isVPS(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            elif stack.pop() != '(':
                return False
    if len(stack) != 0:
        return False
    else:
        return True

t = int(sys.stdin.readline())
for i in range(0, t):
    str1 = sys.stdin.readline().rstrip()
    print('YES' if isVPS(str1) else 'NO')