# no. 1043: 거짓말 (Gold IV)
# 진실을 아는 사람이 파티에 오면 난 무조건 진실만 말해야한다.
# 즉, 파티에 진실을 모르는 사람만 있어야 난 거짓말을 해버릴 수 있다.
# 근데, 내가 파티에서 진실혹은 거짓을 말하면 해당 파티에 참가한 사람들은
# 그것을 기억한다.
# 즉 내가 어떠한 파티에서 4번이 거짓말을 들었는데
# 다른 파티에서 진실을 말한다면 나는 거짓말 쟁이가 되버린다.
# 이러한 점에 유의하여 문제를 풀어야한다.

# 백트래킹 -> 거짓말을 한다~안한다 분기가 생성
# 진실을 말하고자 할때 -> 파티안에 거짓말 들은 사람이 없어야함
# 거짓을 말하고자 할때 -> 파티안에 진실을 들은 사람이 없어야함

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
truth = set()
for i, val in enumerate(map(int, input().split())):
    if i == 0: continue
    truth.add(val)
parties = []
for _ in range(m):
    parties.append(tuple(map(int, input().split()))[1:])

def dfs(i, cur_cnt, truth, lie=None, max_cnt=None):
    if lie == None: lie = set()
    if max_cnt == None: max_cnt = [0]
    if i == m:
        max_cnt[0] = max(max_cnt[0], cur_cnt)
        return max_cnt[0]
    for person in parties[i]:     
        if person in lie: break
    else:
        new_truth = truth.copy()
        for person in parties[i]:
            new_truth.add(person)
        dfs(i+1, cur_cnt, new_truth, lie, max_cnt)
    for person in parties[i]:
        if person in truth: break
    else:
        new_lie = lie.copy()
        for person in parties[i]:
            new_lie.add(person)
        dfs(i+1, cur_cnt+1, truth, new_lie, max_cnt)
    return max_cnt[0]

print(dfs(0, 0, truth))