import sys

def getChocolatePieces(row, column, memo={}):
    if row == 1 and column == 1:
        return 0
    elif column == 1:
        if (row, column) not in memo:
            memo[(row, column)] = 1 + getChocolatePieces(row // 2, column, memo) + getChocolatePieces(row - (row // 2), column, memo)
        return memo[(row, column)]
    else:
        if (row, column) not in memo:
            memo[(row, column)] = 1 + getChocolatePieces(row, column // 2, memo) + getChocolatePieces(row, column-(column // 2), memo)
        return memo[(row, column)]

n, m = map(int, sys.stdin.readline().split())
print(getChocolatePieces(n,m))