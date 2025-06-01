import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
str1 = ''
for num in n:
    str1 += num
print(str1)