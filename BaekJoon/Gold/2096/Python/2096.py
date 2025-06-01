# no. 2096: 내려가기 (Gold V)
# 보자마자 느낌이 dp
# 상태 -> 줄r, 위치(0,1,2)
# mp[r][0] = max(mp[r-1][0], mp[r-1][1])+num[r][0]
# mp[r][1] = max(mp[r-1][0], mp[r-1][1], mp[r-1][2]) + num[r][1]
# mp[r][2] = max(mp[r-1][1], mp[r-1][2]) + num[r]][2]
# 최소 점수는 max -> min 으로 바꾸면된다.

# 메모리 최적화
# 4MB는 생각보다 빡센듯 하다...
# 배열은 한개만 써서 해결했다.

from sys import stdin
input = stdin.readline

n = int(input())
nums = tuple(tuple(map(int, input().split())) for _ in range(n))

mp_i_1 = nums[0]
mp_i = [0, 0, 0]
for i in range(1, n):
    mp_i[0] = max(mp_i_1[0], mp_i_1[1]) + nums[i][0]
    mp_i[1] = max(mp_i_1[0], mp_i_1[1], mp_i_1[2]) + nums[i][1]
    mp_i[2] = max(mp_i_1[1], mp_i_1[2]) + nums[i][2]
    mp_i_1 = mp_i.copy()
    mp_i = [0, 0, 0]
print(max(mp_i_1), end=' ')

mp_i_1 = nums[0]
mp_i = [0, 0, 0]
for i in range(1, n):
    mp_i[0] = min(mp_i_1[0], mp_i_1[1]) + nums[i][0]
    mp_i[1] = min(mp_i_1[0], mp_i_1[1], mp_i_1[2]) + nums[i][1]
    mp_i[2] = min(mp_i_1[1], mp_i_1[2]) + nums[i][2]
    mp_i_1 = mp_i.copy()
    mp_i = [0, 0, 0]
print(min(mp_i_1))