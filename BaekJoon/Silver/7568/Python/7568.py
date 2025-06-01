import sys 

n = int(sys.stdin.readline())
people = []
rank = []
for i in range(0, n):
    people.append(tuple(map(int, sys.stdin.readline().split())))

for i, ival in enumerate(people):
    current_rank = 1
    for j, jval in enumerate(people):
        if i == j:
            continue
        else:   
            if ival[0] < jval[0] and ival[1] < jval[1]:
                current_rank += 1
    rank.append(current_rank)

for val in rank:
    print(val, end=' ')
print('\n', end='')