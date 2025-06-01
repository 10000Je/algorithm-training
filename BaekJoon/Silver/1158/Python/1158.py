import sys

n, k = map(int, sys.stdin.readline().split())
people = [i+1 for i in range(n)]
result = []
current_idx = -1
while people:
    current_idx += k
    if current_idx > len(people)-1:
        current_idx = current_idx % len(people)
    result.append(people.pop(current_idx))
    current_idx -= 1

print('<', end='')
for i, ival in enumerate(result):
    if i != len(result)-1:
        print(ival, ', ', sep='', end='')
    else:
        print(ival, '>', sep='')