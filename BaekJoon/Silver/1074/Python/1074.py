# no. 1074: Z (Silver I)
import sys

def makeZ(row, column, n, start=0):
    if n == 0:
        return start
    else:
        if row < 2**(n-1) and column < 2**(n-1):
            return makeZ(row, column, n-1, start)
        elif row < 2**(n-1) and column >= 2**(n-1):
            return makeZ(row, column - 2**(n-1), n-1, start + 2**(2*n-2))
        elif row >= 2**(n-1) and column < 2**(n-1):
            return makeZ(row - 2**(n-1), column, n-1, start + 2*(2**(2*n-2)))
        else:
            return makeZ(row - 2**(n-1), column - 2**(n-1), n-1, start + 3*(2**(2*n-2)))

n, r, c = map(int, sys.stdin.readline().split())
print(makeZ(r, c, n))