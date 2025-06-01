# no. 1202: 보석 도둑 (Gold II)
# 보석 N개 (m1, v1) , (m2, v2), ... (mn, vn)
# 가방 K개 c1, c2, c3, ... ck

# 각 가방엔 한개의 보석만을 담을 수 있으며
# 담을 수 있는 보석 가격의 합의 최대를 구하자

# 가방을 오름차순으로 정렬해보자
# 보석을 힙의 자료구조로 저장해보자(기준: 보석의 무게)
# 먼저 가방에 담을 수 있는 공들을 최소 힙을 통해 계속 꺼내보자
# 꺼낸 공들은 최대힙에 담아두자
# 더이상 최소 힙에서 꺼낸 보석의 무게가 가방보다 작거나 같지 않다면
# 저장해둔 최대힙에서 보석을 꺼내자, 그러면 최대힙에 다른 보석이 남아있을 것이다.
# 다음 가방은 무조건 이 최대힙 안에 있는 보석들 중 하나를 꺼낼 수 있다. (가방이 최대용량순으로 정렬되어 있으므로)
# 그리고 다음 가방을 선택하고, 위의 과정을 반복하자
# 더이상 보석을 담을 수 없거나, 더이상 담을 가방이 없다면 위 알고리즘을 종료한다.

# 시간복잡도 -> 최소 힙, 최대힙 삽입 과정은 각각 최대 N번, N번 발생한다
# O(2NlogN) -> O(NlogN) 으로 시간복잡도 조건을 충족한다.

import heapq
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())

jewels = []
for _ in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, v))

bags = [int(input()) for _ in range(k)]
bags.sort()

seletable_jewels = []
price_sum = 0
for bag in bags:
    while True:
        if not jewels: break
        jewel = heapq.heappop(jewels)
        m, v = jewel
        if m > bag:
            heapq.heappush(jewels, jewel)
            break
        heapq.heappush(seletable_jewels, (-v, m))
    if not seletable_jewels: continue
    selected_jewel = heapq.heappop(seletable_jewels)
    price_sum += -selected_jewel[0]

print(price_sum)