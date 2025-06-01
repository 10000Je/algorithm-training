import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
max = scores[0]
for score in scores:
    if score > max:
        max = score
sum = 0
for score in scores:
    sum += score/max*100
print(sum/n)
