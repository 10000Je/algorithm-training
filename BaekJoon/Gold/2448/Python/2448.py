# no. 2448: 별 찍기 - 11
# 별을 찍는 문젠데..어떻게 골드4...
# n -> 공백문자를 n-1개 출력
# 분할..정복?
# 24줄은 -> 12줄 별*3개로 분할됨
# 12줄은 -> 6줄 별*3개로 분할됨
# 6줄은 -> 3줄 별*3개로 분할됨

# 하.. 시발... 난이도 이거 골드1~2정도로 올려야됨 ㄹㅇ
# 배열을 이용해 출력을 나중에 하면 된다는 아이디어를 왜 떠올리지 못했는지...
# Z라는 백준 문제와 유사하게 풀리는 문제이다. 분할정복 ㄷㄷ

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

n = int(input())
stars = [[' ' for _ in range(2*n-1)] for _ in range(n)]

def drawstar(n, r, c):
    if n == 3:
        stars[r][c] = '*'
        stars[r+1][c-1] = '*'
        stars[r+1][c+1] = '*'
        for i in range(c-2, c+3):
            stars[r+2][i] = '*'
        return
    drawstar(n//2, r, c)
    drawstar(n//2, r+n//2, c-n//2)
    drawstar(n//2, r+n//2, c+n//2)

drawstar(n, 0, n-1)
for star in stars:
    print(''.join(star))
    print('\n')