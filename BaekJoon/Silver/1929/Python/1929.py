import sys

m, n = map(int, sys.stdin.readline().split())
arr1 = list(range(0, n+1))
arr1[1] = 0
for i in range(2, int(n**(1/2))+1):
    if arr1[i] == 0:
        continue
    for j in range(i*2, n+1, i):
        arr1[j] = 0
for i in range(m, n+1):
    if arr1[i]:
        print(i)