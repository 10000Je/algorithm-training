import sys

n = int(sys.stdin.readline())
pattern = [char for char in sys.stdin.readline().rstrip()]
for _ in range(n-1):
    for idx, char in enumerate(sys.stdin.readline().rstrip()):
        if char != pattern[idx]:
            pattern[idx] = '?'
print(*pattern, sep='')