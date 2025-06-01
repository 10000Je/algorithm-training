import sys

l = int(sys.stdin.readline())
str1 = sys.stdin.readline().rstrip()
memo = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)))
sum = 0
for idx, char in enumerate(str1):
    sum += memo[char] * (31**idx)
print(sum % 1234567891)