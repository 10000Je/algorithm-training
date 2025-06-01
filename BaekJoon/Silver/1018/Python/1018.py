import sys

row, column = map(int, sys.stdin.readline().split())
board = []
for i in range(0, row):
    board.append(sys.stdin.readline().rstrip())

row_pointer = 0
min = None
while row_pointer + 7 < row:
    column_pointer = 0
    while column_pointer + 7 < column:
        chessboard = []
        for i in range(row_pointer, row_pointer+8):
            chessboard.append(board[i][column_pointer:column_pointer+8])
        countVer1 = 0
        countVer2 = 0
        for i, each_row in enumerate(chessboard):
            for j, char in enumerate(each_row):
                if (i+j) % 2 == 0:
                    if char != 'W':
                        countVer1 += 1
                    else:
                        countVer2 += 1
                else:
                    if char != 'B':
                        countVer1 += 1
                    else:
                        countVer2 += 1
        count = countVer1 if countVer1 < countVer2 else countVer2
        if min == None:
            min = count
        else:
            if count < min:
                min = count
        column_pointer += 1
    row_pointer += 1

print(min)
