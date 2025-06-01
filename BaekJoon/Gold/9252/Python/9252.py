# no. 9252: LCS 2 (Gold IV)
# LCS의 길이와 LCS 자체를 "출력"하는 문제

# 두 문자열
# a1 a2 a3 ... an
# b1 b2 b3 ... bm
# 이때 a문자열의 i번째 문자와, b문자열의 j번째 문자가 같다면
# lcs[i][j] = lcs[i-1][j-1]+1
# 만약 다르다면
# lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

# 출력
# 백트래킹 기법이용 -> 배열의 오른쪽 끝에서 부터 이동한다
# i행 j열에서 이동을 시작할때, i-1행 j열, i행 j-1열중
# 더 큰 값이 존재하는 칸으로 이동한다
# 이동한 칸의 두 문자가 "같은" 경우, stack에 푸시후 i-1, j-1칸으로 이동한다
# 0행 또는 0열에 도달할때까지 반복한다

from sys import stdin
input = stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

n, m = len(str1), len(str2)
lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]
for r in range(1, n+1):
    for c in range(1, m+1):
        if str1[r-1] == str2[c-1]:
            lcs[r][c] = lcs[r-1][c-1]+1
        else:
            lcs[r][c] = max(lcs[r-1][c], lcs[r][c-1])

stack = []
r, c = n, m
while r != 0 and c != 0:
    if str1[r-1] == str2[c-1]:
        stack.append(str1[r-1])
        r -= 1
        c -= 1
    else:
        if lcs[r-1][c] > lcs[r][c-1]:
            r -= 1
        else:
            c -= 1
stack.reverse()

print(lcs[n][m])
print(*stack, sep='')