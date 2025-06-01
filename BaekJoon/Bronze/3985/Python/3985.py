import sys
from math import inf

l = int(sys.stdin.readline())
cake = [0 for _ in range(l+1)]
n = int(sys.stdin.readline())
expect_max, expect_idx = -inf, inf

for i in range(1, n+1):
    p, k = map(int, sys.stdin.readline().split())
    if k-p+1 > expect_max:
        expect_max = k-p+1
        expect_idx = i
    elif k-p+1 == expect_max and i < expect_idx:
        expect_idx = i
    for j in range(p, k+1):
        if cake[j] == 0:
            cake[j] = i

cnts = [0 for _ in range(n+1)]
for i in range(1, l+1):
    cnts[cake[i]] += 1

real_max, real_idx = -inf, inf
for i in range(1, n+1):
    if cnts[i] > real_max:
        real_max = cnts[i]
        real_idx = i
    elif cnts[i] == real_max and i < real_idx:
        real_idx = i

print(expect_idx, real_idx, sep='\n')