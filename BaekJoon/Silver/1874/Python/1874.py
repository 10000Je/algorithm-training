import sys

n = int(sys.stdin.readline())
stack = []
str1 = []
memo = {}
push_num = 1
for i in range(0, n):
    num = int(sys.stdin.readline())
    if num in memo:
        str1 = False
        break
    if len(stack) == 0:
        while push_num <= num:
            stack.append(push_num)
            push_num += 1
            str1.append('+')
        memo[stack.pop()] = True
        str1.append('-')
    elif num <= stack[-1]:
        while len(stack) != 0 and num <= stack[-1]:
            memo[stack.pop()] = True
            str1.append('-')
    else:
        while push_num <= num:
            stack.append(push_num)
            push_num += 1
            str1.append('+')
        memo[stack.pop()] = True
        str1.append('-')

if str1:
    for char in str1:
        print(char)
else:
    print('NO')
