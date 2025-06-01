import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
max = 0
for i, ival in enumerate(cards):
    for j, jval in enumerate(cards):
        for k, kval in enumerate(cards):
            if i != j and j != k and k != i and max < ival+jval+kval <= m:
                max = ival+jval+kval
print(max)
