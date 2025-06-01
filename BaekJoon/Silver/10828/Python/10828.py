import sys

n = int(sys.stdin.readline())
stack = []
for i in range(0, n):
    str1 = sys.stdin.readline().rstrip()
    if str1[0:4] == 'push':
        n = int(str1.split().pop())
        stack.append(n)
    elif str1 == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    elif str1 == 'size':
        print(len(stack))
    elif str1 == 'empty':
        print(1 if len(stack) == 0 else 0)
    else:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)