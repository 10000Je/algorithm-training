import sys

n = int(sys.stdin.readline())
arr1 = []
memo = {}
for i in range(0, n):
    num = int(sys.stdin.readline())
    if num not in memo:
        arr1.append(num)
        memo[num] = 1
    else:
        memo[num] += 1

arr1.sort()
for num in arr1:
    for i in range(0, memo[num]):
        print(num)