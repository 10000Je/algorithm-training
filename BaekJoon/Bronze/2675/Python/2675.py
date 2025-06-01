import sys

t = int(sys.stdin.readline())
for i in range(0, t):
    r, s = sys.stdin.readline().split()
    r = int(r)
    for char in s:
        print(char*r, end='')
    print('\n', end='')