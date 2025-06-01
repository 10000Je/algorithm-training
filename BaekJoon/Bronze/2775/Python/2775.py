import sys

def calculate(floor, room, memo={}):
    if floor == 1:
        return ((room) * (room+1))//2
    else:
        sum_of_last_floor = 0
        if (floor, room) not in memo:
            for i in range(1, room+1):
                sum_of_last_floor += calculate(floor-1, i, memo)
            memo[(floor, room)] = sum_of_last_floor
        return memo[(floor, room)]

t = int(sys.stdin.readline())
for i in range(0, t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(calculate(k, n))
