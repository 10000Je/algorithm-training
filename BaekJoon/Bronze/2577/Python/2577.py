import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

num = str(a*b*c)
memo = {}
for char in num:
    if char not in memo:
        memo[char] = 1
    else:
        memo[char] += 1

for n in '0123456789':
    if n not in memo:
        print(0)
    else:
        print(memo[n])
