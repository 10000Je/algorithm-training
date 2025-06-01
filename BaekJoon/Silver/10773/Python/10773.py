import sys

k = int(sys.stdin.readline())
stack = []
for i in range(0, k):
    n = int(sys.stdin.readline())
    if not n:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))