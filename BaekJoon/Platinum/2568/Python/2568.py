# no. 2568: 전깃줄 - 2 (Platinum V)
# 남아있는 모든 전깃줄이 서로 "교차"하지 않게 하기 위해
# 없애야 하는 최소 개수의 전깃줄은?

# A를 오름차순으로 정렬해보자
# 각 A에 대한 B값을 배열로 나타내보자
# 배열은 따로 정렬되지 않은 값들을 가지고 있을 것이다
# 이때 "교차하지 않는다"는 의미는 A에 대한 B의 연결 배열이
# 오름차순으로 나열되어 있다는 의미, 즉 이전 A가 연결되어 있는 B지점 이후로만
# 연결되어 있다는 의미이다. 즉, B배열에서 최장증가부분수열(LIS)을 찾으면
# 그것이 교차하지 않게 하는 A->B의 조합이다.

# 문제에서는 전깃줄의 개수가 100,000까지 가능하므로, dp를 이용한 LIS해법은 사용할 수 없고
# 이진탐색을 이용한 LIS해법을 사용 -> O(NlogN)

# 체감 난이도: P5
# nlogn LIS는 사실 그렇게 어렵지는 않으나, LIS를 사용할 아이디어는 조금 떠올리기 힘들 수
# 있다고는 생각한다. 또 추가로 처리해야될게 많은 문제였다.

from sys import stdin
from bisect import bisect_left
input = stdin.readline

n = int(input())
line_ab = [0 for _ in range(500_001)]
line_ba = [0 for _ in range(500_001)]
for _ in range(n):
    a, b = map(int, input().split())
    line_ab[a] = b
    line_ba[b] = a

nums = []
for b in line_ab:
    if b == 0: continue
    nums.append(b)

lis = []
dp = [0 for _ in range(n)]
for i, b in enumerate(nums):
    idx = bisect_left(lis, b)
    if idx == len(lis):
        lis.append(b)
    else:
        lis[idx] = b
    dp[i] = idx

result_b = set()
idx = n-1
val = len(lis)-1
while idx >= 0:
    if dp[idx] == val:
        result_b.add(nums[idx])
        val -= 1
    idx -= 1

result_a = []
for i, a in enumerate(line_ba):
    if a == 0: continue
    if i in result_b: continue
    result_a.append(a)
result_a.sort()

print(len(nums)-len(lis))
print(*result_a, sep='\n')