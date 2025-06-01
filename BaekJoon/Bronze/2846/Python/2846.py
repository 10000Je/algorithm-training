n = int(input())
heights = [num for num in map(int, input().split())]
stack = []
max_len = 0
for h in heights:
    if not stack:
        stack.append(h)
    else:
        if h > stack[-1]:
            stack.append(h)
            max_len = max(stack[-1] - stack[0], max_len)
        else:
            stack.clear()
            stack.append(h)
print(max_len)