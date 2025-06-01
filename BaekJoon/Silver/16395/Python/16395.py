import sys

def getPascalTriValue(row, column, memo = {}):
    if column == 1 or column == row:
        return 1
    else:
        if (row, column) not in memo:
            memo[(row, column)] = getPascalTriValue(row-1, column-1, memo) + getPascalTriValue(row-1, column, memo)
        return memo[(row, column)]

row, column = map(int, sys.stdin.readline().split())
print(getPascalTriValue(row, column))