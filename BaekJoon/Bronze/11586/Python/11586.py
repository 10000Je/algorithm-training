import sys
n = int(sys.stdin.readline())
arr1 = []
for i in range(0, n):
    arr1.append(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline())
if k == 1:
    for i in range(0, n):
        print(arr1[i])
if k == 2:
    for i in range(0, n):
        print(arr1[i][::-1])
if k == 3:
    for i in range(0, n):
        print(arr1[-1-i])
