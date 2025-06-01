# no. 1806: 부분합 (Gold IV)
# 연속된 수들의 부분합 중 합이 S 이상이 되는 것중,
# 가장 짧은 것의 길이를 구하시오

# 투 포인터!
# 현재 합계가 s보다 작다면, 오른쪽 포인터를 옮겨주고
# s보다 크다면, 왼쪽 포인터를 옮겨준다.

# 그러한 합을 만드는 것이 불가능 하다면 0 을 출력하라.

# 주의할 점, cur_sum 이 0이 되는 경우는 존재할 수 없다.
# 왜냐하면 cur_sum이 0이되면 아무런 숫자가 선택되지 않았다는
# 의미이고, 이는 부분합이라는 전제조건에 위배된다.

from sys import stdin
input = stdin.readline

n, s = map(int, input().split())
nums = tuple(map(int, input().split()))

i = j = 0
cur_sum = nums[0]
min_len = 10**5

while True:
    if cur_sum < s:
        j += 1
        if j >= n: break
        cur_sum += nums[j]
    else:
        min_len = min(min_len, j-i+1)
        if i == j: break
        i += 1
        cur_sum -= nums[i-1]

if min_len == 10**5:
    print(0)
else:
    print(min_len)