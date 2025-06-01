equation = input()
nums = list()
stack = list()
current_sum = 0
for char in reversed(equation):
    n = str()
    if char in '+-':
        while stack:
            n += stack.pop()
        nums.append(int(n))
        if char == '-':
            current_sum += (-1 * sum(nums))
            nums.clear()
    else:
        stack.append(char)
n = str()
while stack:
    n += stack.pop()
nums.append(int(n))

current_sum += sum(nums)
print(current_sum)

# split을 써서 더 간결하게 만드는 것도 가능