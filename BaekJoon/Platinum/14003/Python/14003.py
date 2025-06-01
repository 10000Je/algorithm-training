# no. 14003: 가장 긴 증가하는 부분 수열 5 (Platinum 5)
# LIS의 길이를 출력하고, LIS를 출력하시오 답이 여러개인 경우는 아무거나 출력하시오

# 잘 알려진 문제 중 하나로, 이분탐색을 이용한 LIS문제이다
# LIS의 출력방법은 dp에서의 풀이를 참고해볼 수 있다.
# dp로 풀때, dp테이블에는 각 숫자가 가질 수 있는 LIS길이가 담긴다.
# 그렇다면 LIS 길이가 증가하는 값을 고를때마다 dp테이블에서 값이 증가하는 형태이고,
# 그럼 이 dp 테이블을 역순으로 순회하며 "가장 큰 값을" 가지는 인덱스부터
# 차례대로 하나씩 감소하는 값들을 역추적하여 이를 출력하면 LIS 배열이 되지 않을까?

# dp 해법에서는 이 테이블자체가 dp를 수행하면서 만들어지지만, 이분탐색에서는 따로
# 만들어지지 않으므로, 우리가 직접 만들어야한다.
# 이분탐색을 수행해서 lis 배열에 숫자를 덮어씌우는 "위치", 즉 인덱스 값을 얻는다.
# 이는 dp 해법에서의 각 숫자가 가질 수 있는 LIS길이를 의미한다.
# 따라서 dp 테이블처럼 동일하게, 배열에 값을 덮어쓰거나 추가할때마다 인덱스 값을
# 기록한다면, dp 해법에서처럼 동일한 방법으로 LIS 배열을 출력할 수 있을 것이다.

# 체감 난이도: G2
# 사실 이 모든 개념을 처음부터 떠올려야 한다면 당연히 P5 정도 되겠지만, 이 문제는
# 좀 유명한 문제이기도 하다. 기본적으로 LIS를 접할때 LIS의 출력방법도 같이 
# 찾아보기 때문에 아이디어만 갖고 있다면 쉽게 풀 수 있는 문제이다.

from sys import stdin
input = stdin.readline

n = int(input())
nums = tuple(map(int, input().split()))

def bisect(arr, value, left=None, right=None):
    if left == None: left = 0
    if right == None: right = len(arr)-1
    if left > right:
        return left
    mid = (left+right)//2
    if arr[mid] >= value:
        return bisect(arr, value, left, mid-1)
    else:
        return bisect(arr, value, mid+1, right)

lis = []
dp = [0 for _ in range(n)]

for i, num in enumerate(nums):
    idx = bisect(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num
    dp[i] = idx

stack = []
cur_idx = len(lis)-1
for i in reversed(range(n)):
    if dp[i] == cur_idx:
        stack.append(nums[i])
        cur_idx -= 1
stack.reverse()

print(len(lis))
print(*stack)
    