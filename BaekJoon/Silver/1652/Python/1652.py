import sys

n = int(sys.stdin.readline())
room = [[cell for cell in sys.stdin.readline().rstrip()] for _ in range(n)]

width = length = cnt = 0
for row in range(n):
    for col in range(n):
        if room[row][col] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                width += 1
            cnt = 0
    if cnt >= 2:
        width += 1
    cnt = 0

cnt = 0
for col in range(n):
    for row in range(n):
        if room[row][col] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                length += 1
            cnt = 0
    if cnt >= 2:
        length += 1
    cnt = 0

print(width, length)
