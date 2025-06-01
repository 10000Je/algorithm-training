n, p = map(int, input().split())
memo = {}
idx = 1
cur_num = n
while cur_num not in memo:
    memo[cur_num] = idx
    cur_num = cur_num * n % p
    idx += 1
print(idx-memo[cur_num])