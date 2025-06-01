import sys

n, m = map(int, sys.stdin.readline().split())
a = [[num for num in map(int, sys.stdin.readline().split())] for _ in range(n)]
m, k = map(int, sys.stdin.readline().split())
b = [[num for num in map(int, sys.stdin.readline().split())] for _ in range(m)]

multipled_matrix = [[0 for _ in range(k)] for _ in range(n)]
for row in range(n):
    for col in range(k):
        for i in range(m):
            multipled_matrix[row][col] += a[row][i] * b[i][col]
for row in multipled_matrix:
    print(*row, sep=' ')