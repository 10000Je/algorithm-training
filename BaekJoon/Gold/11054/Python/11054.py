# no. 11054: 가장 긴 바이토닉 부분 수열
# Sk 를 기준으로 왼쪽은 오름차순, 오른쪽은 내림차순으로 숫자가 존재하는 수열이다.
# Sk 를 기준으로 잡았을때의 바이토닉 부분 수열의 길이는
# S1-Sk-1 까지의 최장증가부분수열의 길이 + 
# Sk+1-sn 까지의 최장감소부분수열의 길이(사실 sn-sk+1 까지의 최장증가부분수열임) + 1 이다.
# LBS(k) = LIS(k) + LMS(k) ... 하지만 Sk가 LIS에도 LMS에도 포함되면 -1 해줘야함
# 최장증가부분수열(LIS) 는 어떻게 정의될까?
# a1, a2, a3, .. an
# k 번째 숫자를 탐색할때
# k가 LIS수열의 마지막 숫자보다 크다면
# 1부터 k-1(i)까지의 루프
# LIS(k) = max(LIS(k), LIS(i)+1) if ak > ai 
# LMS(k) = max(LMS(k), LMS(i)+1) if ak < ai

import sys
input = sys.stdin.readline

n = int(input())
a = tuple(map(int, input().split()))

lis = [0 for _ in range(n)]
lds = [0 for _ in range(n)]
lbs = [0 for _ in range(n)]

for k in range(n):
    lis[k] = 1
    for i in range(k):
        if a[k] > a[i]:
            lis[k] = max(lis[k], lis[i]+1)

for k in range(n-1, -1, -1):
    lds[k] = 1
    for i in range(n-1, k, -1):
        if a[k] > a[i]:
            lds[k] = max(lds[k], lds[i]+1)

lbs[0] = lds[0]
lbs[n-1] = lis[n-1]
for k in range(1, n-1):
    lbs[k] = lis[k] + lds[k] - 1

print(max(lbs))