import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a = [num for num in map(int, sys.stdin.readline().split())][1:]
    b = [num for num in map(int, sys.stdin.readline().split())][1:]
    if a.count(4) != b.count(4):
        print('A' if a.count(4) > b.count(4) else 'B')
    elif a.count(3) != b.count(3):
        print('A' if a.count(3) > b.count(3) else 'B')
    elif a.count(2) != b.count(2):
        print('A' if a.count(2) > b.count(2) else 'B')
    elif a.count(1) != b.count(1):
        print('A' if a.count(1) > b.count(1) else 'B')
    else:
        print('D')