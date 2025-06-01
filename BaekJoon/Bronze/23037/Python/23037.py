import sys

n = sys.stdin.readline().rstrip()
sum = 0
for char in n:
    sum += int(char)**5
print(sum)