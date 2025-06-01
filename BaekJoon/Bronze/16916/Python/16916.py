import sys

p = sys.stdin.readline().rstrip()
s = sys.stdin.readline().rstrip()

if s in p:
    print(1)
else:
    print(0)