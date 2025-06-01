n = int(input())
m = int(input())
s = input()

stack = []
cnt = 0
for char in s:
    if char == 'I' and (not stack or stack[-1] == 'O'):
        stack.append(char)
        if len(stack) == 2*n+1:
            cnt += 1
            del stack[:-3:-1]
    elif char == 'I':
        stack.clear()
        stack.append(char)
    elif char == 'O' and (stack and stack[-1] == 'I'):
        stack.append(char)
    else:
        stack.clear()
print(cnt)