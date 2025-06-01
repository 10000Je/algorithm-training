import sys

n = int(sys.stdin.readline())
creator = None
for i in range(1, n+1):
    str1 = str(i)
    sum = i
    for j in str1:
        sum += int(j)
    if sum == n:
        creator = i
        break
print(creator or 0)