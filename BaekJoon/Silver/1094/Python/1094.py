import heapq

x = int(input())
sticks = [64]
while sum(sticks) > x:
    min_stick = heapq.heappop(sticks)
    heapq.heappush(sticks, min_stick // 2)
    if sum(sticks) < x:
        heapq.heappush(sticks, min_stick // 2)

print(len(sticks))
