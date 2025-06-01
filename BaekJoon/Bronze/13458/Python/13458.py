import sys

n = int(sys.stdin.readline())
testers = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
cnt = 0
for tester in testers:
    cnt += 1
    tester -= b
    if tester > 0:
        cnt += (tester // c) if not tester % c else (tester // c) + 1
print(cnt)
