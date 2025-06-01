# no. 15654: N과 M (5)
# 중복되는 수열 출력X, 수열은 사전 순으로 증가하는 순서로 출력
# [1, 8]과 [8, 1]은 다른 수열, 즉 순서 상관 있음.
# 리스트에 값을 append, pop 하는 방식으로 수열을 만들어줌
# 다만 맨 처음 재귀의 루프문이 종료되는 시점에는 cur_sequence에는
# 아무것도 남아 있지 않으므로 이를 체크하는 구문이 필요함

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = tuple(map(int, input().split()))

def dfs(depth=m, cur_sequence=[], sequences=[]):
    if depth == 0:
        sequences.append(cur_sequence.copy())
        cur_sequence.pop()
        return
    for num in nums:
        if num in cur_sequence:
            continue
        cur_sequence.append(num)
        dfs(depth-1, cur_sequence, sequences)
    if cur_sequence:
        cur_sequence.pop()
    return sequences

seq = dfs()
seq.sort()
for arr in seq:
    print(*arr)