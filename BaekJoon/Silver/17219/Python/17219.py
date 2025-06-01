import sys

n, m = map(int, sys.stdin.readline().split())
memo = {}
for _ in range(n):
    address, pw = sys.stdin.readline().split()
    memo[address] = pw
for _ in range(m):
    address = sys.stdin.readline().rstrip()
    print(memo[address])