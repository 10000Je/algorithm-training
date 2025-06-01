# no. 15666: N과 M (12)
# 같은 수를 여러번 골라도 된다.
# 고른 수열은 비내림차순 이여야한다.
# 주의할 점: 입력으로 주어지는 수에 중복되는 수가 있을 수 있다.
# 이때 같은 수를 중복으로 뽑는것이 가능하므로 입력으로 주어지는 수에서 중복되는 수는 없애주자

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = set(map(int, input().split()))

def dfs(cur_seq=None, seqs=None):
    if cur_seq == None: cur_seq = []
    if seqs == None: seqs = []
    if len(cur_seq) == m:
        seqs.append(cur_seq.copy())
        cur_seq.pop()
        return
    for num in nums:
        if not cur_seq or cur_seq[-1] <= num:
            cur_seq.append(num)
            dfs(cur_seq, seqs)
    if cur_seq: cur_seq.pop()
    return seqs

seqs = dfs()
seqs.sort()
for seq in seqs:
    print(*seq)