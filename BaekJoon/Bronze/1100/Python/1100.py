board = [[char for char in input()] for _ in range(8)]
cnt = 0
for row in range(len(board)):
    for col in range(len(board[row])):
        if (row + col) % 2 == 0 and board[row][col] == 'F':
            cnt += 1
print(cnt)
