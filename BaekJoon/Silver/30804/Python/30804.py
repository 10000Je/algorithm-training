# no. 30804: 과일 탕후루 (Silver II)
# 투포인터?

from sys import stdin
input = stdin.readline

n = int(input())
fruits = tuple(map(int, input().split()))

i = j = 0
tanghuru = {fruits[0]: 1}
cnt = 1

while True:
    if j == n-1:
        break
    if len(tanghuru) == 2 and fruits[j+1] not in tanghuru:
        i += 1
        tanghuru[fruits[i-1]] -= 1
        if tanghuru[fruits[i-1]] == 0:
            del tanghuru[fruits[i-1]]
    else:
        j += 1
        if fruits[j] in tanghuru:
            tanghuru[fruits[j]] += 1
        else:
            tanghuru[fruits[j]] = 1
        cnt = max(cnt, sum(tanghuru.values()))

print(cnt)