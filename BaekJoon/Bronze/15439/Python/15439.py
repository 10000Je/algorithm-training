import sys
n = int(sys.stdin.readline().rstrip())
combination = 0
for i in range(0, n):
    for j in range(0, n):
        if i != j:
            combination += 1
print(combination)