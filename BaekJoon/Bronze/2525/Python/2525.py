import sys
h,m = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().strip())
ch = c // 60
cm = c % 60

m += cm
if m >= 60:
    m -= 60
    h += 1
h += ch
h = h % 24

print(h, m)