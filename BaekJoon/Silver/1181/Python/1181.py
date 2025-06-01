import sys

n = int(sys.stdin.readline())
arr1 = []
memo = {}
for i in range(0, n):
    str1 = sys.stdin.readline().rstrip()
    if str1 not in memo:
        memo[str1] = True
        arr1.append(str1)

arr1.sort(key = lambda x: (len(x), x))
for i in arr1:
    print(i)