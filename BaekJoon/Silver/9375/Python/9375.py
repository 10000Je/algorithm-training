import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        c_name, c_type = sys.stdin.readline().split()
        if c_type not in clothes:
            clothes[c_type] = [c_name]
        else:
            clothes[c_type].append(c_name)
    cnt = 1
    for key in clothes.keys():
        cnt = cnt * (len(clothes[key])+1)
    print(cnt-1)