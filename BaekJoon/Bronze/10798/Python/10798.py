board = [[char for char in input()] for _ in range(5)]
max_len = max(map(len, board))
new_str = []
for i in range(max_len):
    for j in range(5):
        if i < len(board[j]):
            new_str.append(board[j][i])
print(*new_str, sep='')