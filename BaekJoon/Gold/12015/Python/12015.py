# no. 12015: 가장 긴 증가하는 부분 수열 2 (Gold II)
# LIS 문제긴 한데, N <= 1_000_000 이라, 일반적인 dp 알고리즘으론 못푼다
# 이분탐색을 이용한 해법을 적용해야 하며, 파이썬의 bisect 모듈의 bisect_left 함수를
# 이용하면 쉽게 풀 수 있다.

from sys import stdin
from bisect import bisect_left
input = stdin.readline

n = int(input())
nums = tuple(map(int, input().split()))
lis = [nums[0]]
for i in range(1, n):
    idx = bisect_left(lis, nums[i])
    if idx == len(lis):
        lis.append(nums[i])
    else:
        lis[idx] = nums[i]

print(len(lis))