# no. 15657: N과 M (8) (Silver III)
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러번 고를 수 있음 (중복 가능)
# 비내림차순 이여야함
# 백트래킹

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = tuple(map(int, input().split()))

def dfs(cur_seq=None, seqs=None):
    if cur_seq == None:
        cur_seq = []
    if seqs == None:
        seqs = []
    if len(cur_seq) == m:
        seqs.append(cur_seq.copy())
        cur_seq.pop()
        return
    for num in nums:
        if not cur_seq or num >= cur_seq[-1]:
            cur_seq.append(num)
            dfs(cur_seq, seqs)
    if cur_seq:
        cur_seq.pop()
    return seqs

seqs = dfs()
seqs.sort()
for seq in seqs:
    print(*seq)