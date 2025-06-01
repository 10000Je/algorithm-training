import sys

a, b, v = map(int, sys.stdin.readline().split())
elapsed_days =  (v-a) // (a-b) + 2 if (v-a) % (a-b) != 0 else (v-a) // (a-b) + 1
print(elapsed_days)