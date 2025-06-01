# no. 21395: 연속한 소수 만들기
# 사실 왜 이 풀이가 맞는지에 대한 증명은 하질 못하겠다
# 다만, 테스트 케이스를 도입해보았을 때, 정렬 했을 때 가장 작은 숫자가
# 연속된 소수의 가장 작은 숫자로 대입이 되어야 최소값이 된다는 것을 파악.
# xi의 값의 범위가 <=100,000 이고, n이 200이므로, 슬라이딩 윈도우 방식으로
# 브루트-포싱 진행, 최소값 도출
# 계속 이 풀이를 생각하긴 했지만, 왜 되는지는 도저히 모르겠다.

# 체감 난이도: G4

from sys import stdin
from math import inf, sqrt
input = stdin.readline
XI_MAX = 150_000

t = int(input())
for _ in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()

    tmp = [i for i in range(XI_MAX)]
    tmp[1] = 0
    for i in range(2, (int)(sqrt(XI_MAX))+1):
        j = i*2
        while j < XI_MAX:
            tmp[j] = 0
            j += i
    prime_nums = []
    for i in range(XI_MAX):
        if tmp[i] != 0:
            prime_nums.append(i)
    
    min_sum = inf
    for i in range(len(prime_nums)-n):
        cur_sum = 0
        for j in range(n):
            cur_sum += abs(x[j]-prime_nums[i+j])
        min_sum = min(min_sum, cur_sum)
    print(min_sum)