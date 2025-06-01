import sys

input = sys.stdin.readline
board = [[0 for _ in range(1001)] for _ in range(1001)]
n = int(input())
for i in range(1, n+1):
    col_start, row_start, width, height = map(int, input().split())
    for col in range(col_start, col_start+width):
        for row in range(row_start, row_start+height):
            board[col][row] = i

areas = [0 for _ in range(n+1)]
for col in range(1001):
    for row in range(1001):
        areas[board[col][row]] += 1

print(*areas[1:], sep='\n')