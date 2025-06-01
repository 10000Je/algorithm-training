import sys

def dist(type1, type2, type3):
    d1 = 0
    for i in range(4):
        if type1[i] != type2[i]:
            d1 += 1
    d2 = 0
    for i in range(4):
        if type2[i] != type3[i]:
            d2 += 1
    d3 = 0
    for i in range(4):
        if type1[i] != type3[i]:
            d3 += 1
    return d1 + d2 + d3

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    memo = {}
    for mbti in sys.stdin.readline().split():
        if mbti not in memo:
            memo[mbti] = 1
        else:
            memo[mbti] += 1
    cur_dist = float('inf')
    for a in memo.keys():
        for b in memo.keys():
            for c in memo.keys():
                if a == b and b == c and c == a:
                    if memo[a] < 3:
                        continue
                elif a == b:
                    if memo[a] < 2:
                        continue
                elif b == c:
                    if memo[b] < 2:
                        continue
                elif a == c:
                    if memo[a] < 2:
                        continue
                cur_dist = min(cur_dist, dist(a,b,c))
    print(cur_dist)
