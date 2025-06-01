import sys

n, m = map(int, sys.stdin.readline().split())
paper = [[num for num in map(int, sys.stdin.readline().split())] for i in range(n)]
max_sum = 0
for row in range(len(paper)):
    for col in range(len(paper[row])):
        tetrominos = [
            [(row, col), (row, col+1), (row, col+2), (row, col+3)],
            [(row, col), (row+1, col), (row+2, col), (row+3, col)],
            [(row, col), (row, col+1), (row+1, col), (row+1, col+1)],
            [(row, col), (row+1, col), (row+2, col), (row+2, col+1)],
            [(row, col), (row, col-1), (row, col-2), (row+1, col-2)],
            [(row, col), (row-1, col), (row-2, col), (row-2, col-1)],
            [(row, col), (row, col+1), (row, col+2), (row-1, col+2)],
            [(row, col), (row+1, col), (row+2, col), (row+2, col-1)],
            [(row, col), (row-1, col), (row, col+1), (row, col+2)],
            [(row, col), (row, col+1), (row, col+2), (row+1, col+2)],
            [(row, col), (row-1, col), (row-2, col), (row-2, col+1)],
            [(row, col), (row+1, col), (row+1, col+1), (row+2, col+1)],
            [(row, col), (row, col+1), (row-1, col+1), (row-1, col+2)],
            [(row, col), (row-1, col), (row-1, col+1), (row-2, col+1)],
            [(row, col), (row, col+1), (row+1, col+1), (row+1, col+2)],
            [(row, col), (row, col+1), (row+1, col+1), (row, col+2)],
            [(row, col), (row, col+1), (row-1, col+1), (row+1, col+1)],
            [(row, col), (row, col+1), (row-1, col+1), (row, col+2)],
            [(row, col), (row+1, col), (row+1, col+1), (row+2, col)]
        ]
        for tetromino in tetrominos:
            cnt = 0
            for tm_row, tm_col in tetromino:
                if tm_row < 0 or tm_row >= len(paper):
                    break
                if tm_col < 0 or tm_col >= len(paper[tm_row]):
                    break
                cnt += paper[tm_row][tm_col]
            else:
                if cnt > max_sum:
                    max_sum = cnt
print(max_sum)