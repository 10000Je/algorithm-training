# no. 30805: 사전 순 최대 공통 부분 수열 (Gold IV)
# A와 B의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기 K를 구하시오
# 조건, N과 M이 100보다 작다
# 1. 공통 부분 수열의 첫 수가 가장 큰놈이 사전순으로 나중에 온다
# 2. 첫 수가 정해졌으면 그 다음 수가 가장 큰놈이 사전 순으로 나중에 온다
# 3. 더이상 공통 수가 없을 때까지 이 과정을 반복하면, 사전 순으로 가장 나중인 수열이 나온다

from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a_set, b_set = set(a), set(b)
intersec = a_set & b_set
lcs = []
while intersec:
    num = max(intersec)
    lcs.append(num)
    ai, bi = a.index(num), b.index(num)
    del a[:ai+1]
    del b[:bi+1]
    a_set, b_set = set(a), set(b)
    intersec = a_set & b_set

print(len(lcs))
print(*lcs)
