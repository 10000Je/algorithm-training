# no. 2467: 용액 (Gold V)
# two-pointer 접근

# 후기 -> 체감난이도 (Silver I)
# 생각보다 너무 쉬운 문제였다.
# 투포인터 아이디어 떠올리는 것도 매우 쉬웠고
# 구현난이도도 높지 않았다.

from sys import stdin
input = stdin.readline

n = int(input())
sols = tuple(map(int, input().split()))

left, right = 0, n-1
cur_pair = (sols[0], sols[n-1])
while left < right:
    sol1, sol2 = cur_pair
    if abs(sols[left]+sols[right]) < abs(sol1+sol2):
        cur_pair = (sols[left], sols[right])
    if sols[left] + sols[right] > 0:
        right -= 1
    elif sols[left] + sols[right] < 0:
        left += 1
    else:
        break

print(*cur_pair)