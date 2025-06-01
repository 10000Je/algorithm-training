import sys

a, b, c = map(int, sys.stdin.readline().split())
while not (a == 0 and b == 0 and c == 0):
    if a >= b and a >= c:
        if b ** 2 + c ** 2 == a ** 2:
            print('right')
        else:
            print('wrong')
    elif b >= a and b >= c:
        if a ** 2 + c ** 2 == b ** 2:
            print('right')
        else:
            print('wrong')
    else:
        if a ** 2 + b ** 2 == c ** 2:
            print('right')
        else:
            print('wrong')
    a, b, c = map(int, sys.stdin.readline().split())