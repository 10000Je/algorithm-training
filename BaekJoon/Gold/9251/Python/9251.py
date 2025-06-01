# no. 9251: LCS (Gold V)

# LCS 최장공통 부분수열 문제.
# 대표적인 동적 프로그래밍 문제중 하나이다.
# 두 수열이 존재한다고 가정해보자
# a1, a2, a3, ..., an (길이가 n)
# b1, b2, b3, ..., bm (길이가 m)
# 그리고 LCS 수열이 존재한다고 해보자.
# l1, l2, l3, ..., lk (길이가 k)
# 만약 an과 bm이 같다면? (an == bm)
#   LCS(an, bm) = LCS(an-1, bn-1)+an(또는 bm)
# 만약 an과 bm이 다르다면? (an != bm)
#   lk가 an이 아닌경우 (lk != an)
#       LCS(an, bm) = LCS(an-1, bm)
#   lk가 bm이 아닌경우 (lk != bm)
#       LCS(an, bm) = LCS(an, bn-1)
# 참고> an과 bm이 다를경우 lk는 am도 bm도 아닌거 아닌가요? 최장수열에 못들어 가잖아요!
#   : an과 bm이 다르더라도 an-1과 bm이 같다면 이 경우 bm이 최장수열에 들어갈 수 있고,
#   마찬가지로 an과 bm-1이 같다면 이 경우 an이 최장수열에 들어갈 수 있기 때문에,
#   두가지 경우의 수를 고려해줘야 한다.
#       LCS(an, bm) = max(LCS(an-1, bm), LCS(an, bn-1))
# 두 가지 경우중 최대값이 길이가 긴쪽이 최장수열일 것이다.
# 우리는 lcs의 길이만 구하면 된다.
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
n, m = len(str1), len(str2)
lcs = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[n][m])