import sys

h,m = map(int, sys.stdin.readline().split())
if m >= 45:
    m -= 45
else:
    h -= 1
    if h < 0:
        h += 24
    m += 15
print(h,m)