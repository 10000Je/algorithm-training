# no. 21867: Java Bitecode

n = int(input())
_str = input()

stack = []
for char in _str:
    if char == 'J' or char == 'A' or char == 'V':
        continue
    stack.append(char)

if stack:
    print(*stack, sep='')
else:
    print("nojava")