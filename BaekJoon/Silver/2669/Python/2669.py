rectengles = []
board = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[x][y] = 1
area = 0
for x in range(1, 101):
    for y in range(1, 101):
        if board[x][y]:
            area += 1
print(area)
