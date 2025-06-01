import sys

n = int(sys.stdin.readline())
arr1 = []
for i in range(0, n):
    arr1.append(int(sys.stdin.readline()))
arr1.sort()
for val in arr1:
    print(val)