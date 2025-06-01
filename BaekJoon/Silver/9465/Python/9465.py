# no. 9465: 스티커 (Silver I)
# (b) 그림을 보자.
# 만약 내가 100이 적혀 있는 스티커를 떼었을 때?
# 즉 0행 2열에 있는 스티커를 뜯었다 가정해보자.
# 이 경우, 이 스티커를 뜯은 경우의 점수의 최대값은
# 0행 1열, 1행 2열, 0행 3열을 제외하고 나머지 스티커를 뜯은 경우중 최대값에
# 현재 스티커의 점수 100을 더한 값이다.
# 최대점수를 MP 라고 표현해보자.
# 이걸 어떻게 동적 프로그래밍 적으로 접근하지...
# (결국 힌트 봄 ㅅㅂ 지그재그가 힌트임)
# 2행 n열의 스티커를 뽑았을때
# 1) 1행 n-1의 스티커를 뽑는 경우
# MP(2, n) = 값 + MP(1, n-1)
# 2) 1행 n-1의 스티커를 뽑지 않는 경우 
# MP(2, n) = 값 + max(MP(1, n-2), MP(2, n-2))

# 1행 n열의 스티커를 뽑았을때
# 1) 2행 n-1의 스티커를 뽑는 경우
# MP(1, n) = 값 + MP(2, n-1)
# 2) 2행 n-1의 스티커를 뽑지 않는 경우
# MP(1, n) = 값 + max(MP(2, n-2), MP(1, n-2))

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    mp = [[0 for _ in range(n)] for _ in range(2)]
    mp[0][0], mp[1][0] = stickers[0][0], stickers[1][0]
    if n >= 2:
        mp[0][1], mp[1][1] = stickers[0][1] + mp[1][0], stickers[1][1] + mp[0][0]
    for c in range(2, n):
        mp[0][c] = max(stickers[0][c] + mp[1][c-1], stickers[0][c]+max(mp[0][c-2], mp[1][c-2]))
        mp[1][c] = max(stickers[1][c] + mp[0][c-1], stickers[1][c]+max(mp[0][c-2], mp[1][c-2]))
    print(max(mp[0][n-1], mp[1][n-1]))