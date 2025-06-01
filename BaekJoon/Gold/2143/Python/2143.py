# no. 2143: 두 배열의 합 (Gold III)
# 두 배열의 부분합을 각각 S1, S2라 하자
# S1+S2가 T가 되는 경우의 수를 구하라
# sum_a[i][j] -> i번째 숫자~j번째 숫자 부분합
# sum_a[i][j] = sum_a[0][j] - sum_a[0][i-1] -> dp

# a의 부분합들을 해쉬맵에 저장한다. 합 -> 합이 등장한 횟수
# a의 키를 루프하여, 키의 값이 k일 경우, b의 부분합들을 저장한 해쉬맵에서
# t-k키 값의 경우의 수를 룩업하여, 두 값을 곱해준 값을 매번 더해주면 된다

# 체감 난이도: Gold IV -> 아이디어가 상당히 고급스러운 문제다
# 근데 네 수의 합이라는 문제를 풀면서 유사한 방식으로 접근해본 기억이 있었기
# 때문에 더 쉽게 푼 것도 있긴 했다.

from sys import stdin
input = stdin.readline

t = int(input())
n = int(input())
a = tuple(map(int, input().split()))
m = int(input())
b = tuple(map(int, input().split()))

sum_a = [[0 for _ in range(n)] for _ in range(n)]
map_a = {}
tmp = 0
for i in range(n):
    tmp += a[i]
    sum_a[0][i] = tmp
    if sum_a[0][i] not in map_a:
        map_a[sum_a[0][i]] = 1
    else:
        map_a[sum_a[0][i]] += 1

for i in range(1, n):
    for j in range(i, n):
        sum_a[i][j] = sum_a[0][j] - sum_a[0][i-1]
        if sum_a[i][j] not in map_a:
            map_a[sum_a[i][j]] = 1
        else:
            map_a[sum_a[i][j]] += 1

sum_b = [[0 for _ in range(m)] for _ in range(m)]
map_b = {}
tmp = 0
for i in range(m):
    tmp += b[i]
    sum_b[0][i] = tmp
    if sum_b[0][i] not in map_b:
        map_b[sum_b[0][i]] = 1
    else:
        map_b[sum_b[0][i]] += 1

for i in range(1, m):
    for j in range(i, m):
        sum_b[i][j] = sum_b[0][j] - sum_b[0][i-1]
        if sum_b[i][j] not in map_b:
            map_b[sum_b[i][j]] = 1
        else:
            map_b[sum_b[i][j]] += 1

result = 0
for k, cnt in map_a.items():
    if t-k not in map_b:
        continue
    else:
        result += cnt*map_b[t-k]

print(result)