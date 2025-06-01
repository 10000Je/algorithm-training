# no. 15663: N과 M (9)
# 백트래킹
# 같은 숫자를 여러번 뽑아도 되지만, 중복되는 수열은 출력X
# 4 4 2 같은 수열이 가능하다는 뜻

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = {}
for num in map(int, input().split()):
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] += 1

def dfs(depth=m, cur_sequence=[], sequences=[]):
    if depth == 0:
        sequences.append(cur_sequence.copy())
        cur_sequence.pop()
        return
    for num in nums:
        if cur_sequence.count(num) == nums[num]:
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