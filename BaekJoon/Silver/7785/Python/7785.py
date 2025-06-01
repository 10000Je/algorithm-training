import sys

n = int(sys.stdin.readline())
memo = {}
for _ in range(n):
    name, act = sys.stdin.readline().split()
    memo[name] = act

cur_employees = [name for name, act in memo.items() if act == 'enter']
cur_employees.sort(reverse=True)
print(*cur_employees, sep='\n')