import sys

t = int(sys.stdin.readline())
for i in range(0, t):
    h, w, n = map(int, sys.stdin.readline().split())
    floor =  n % h if n % h != 0 else h
    number = (n // h) if n % h == 0 else (n // h) + 1
    room = 100 * floor + number
    print(room)