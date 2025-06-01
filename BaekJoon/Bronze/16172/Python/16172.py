import sys

s = sys.stdin.readline().rstrip()
k = sys.stdin.readline().rstrip()

for i in range(0, 10):
    s = s.replace(str(i), '')

print(1 if k in s else 0)