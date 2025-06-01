# no. 7453: 합이 0인 네 정수
# A, B배열의 합을 딕셔너리에 저장하고, C, D배열의 합을 딕셔너리에 저장한다.
# 그럼 각각 최대 16_000_000 경우의 수의 합이 저장될 것이고
# 한 딕셔너리를 루프한다고 가정하고, 현재 루프하고 있는 합이 c라고 해보자
# 그럼 나머지 딕셔너리에서 합이 -c인 값을 O(1)안에 불러와 두개의 경우의 수를
# 각각 곱하면 해당 루프에서의 합이 0인 경우의 수 찾기는 완료
# 이제 16_000_000 가지의 경우의 수에 대해서 경우의 수를 찾아 전부다 합하면 끝

# 후기: 투포인터로 다 풀고나서야 깨달았다...
# 쓸데없는 루프만 줄이면 된다는것을...이제야 꺠달아요

from sys import stdin
input = stdin.readline

n = int(input())
a, b, c, d = [], [], [], []

for _ in range(n):
    i, j, k, l = map(int, input().split())
    a.append(i)
    b.append(j)
    c.append(k)
    d.append(l)

cd = {}
for cval in c:
    for dval in d:
        if cval+dval not in cd:
            cd[cval+dval] = 1
        else:
            cd[cval+dval] += 1

cnt = 0
for aval in a:
    for bval in b:
        if -(aval+bval) in cd:
            cnt += cd[-(aval+bval)]

print(cnt)