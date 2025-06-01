import sys

n, k = map(int, sys.stdin.readline().split())
countries = []
for _ in range(n):
    idx, gold, silver, bronze = map(int, sys.stdin.readline().split())
    countries.append((idx, gold, silver, bronze))
countries.sort(key=lambda x:(x[1], x[2], x[3]), reverse=True)

rank = [0 for _ in range(n)]
rank[0] = 1
for i in range(len(countries)):
    if countries[i-1][1:] == countries[i][1:]:
        rank[i] = rank[i-1]
    else:
        rank[i] = i+1
    if countries[i][0] == k:
        print(rank[i])
        break