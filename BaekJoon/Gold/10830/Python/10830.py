# no. 10830: 행렬 제곱 (Gold IV)
# 분할정복
# 입력으로 주어지는 행렬의 각 숫자가 1000보다 "작거나 같은 것에" 주의하자.

from sys import stdin
input = stdin.readline
r = 1000

n, b = map(int, input().split())
matrix = [[num%r for num in map(int, input().split())] for _ in range(n)]

def multiple(a, b):
    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_matrix[i][j] += (a[i][k]%r)*(b[k][j]%r)%r  
            new_matrix[i][j] %= r
    return new_matrix

def power(a, n):
    if n == 1:
        return a
    tmp = power(a, n//2)
    if n % 2:
        return multiple(multiple(tmp, tmp), a)
    else:
        return multiple(tmp, tmp)

result = power(matrix, b)
for arr in result:
    print(*arr)