import sys
import heapq

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    min_heap, max_heap = [], []
    memo = {}
    for j in range(k):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -1*num)
            memo[num] = 1 if num not in memo else memo[num] + 1
        if cmd == 'D':
            if num == -1:
                if not min_heap:
                    continue
                val = heapq.heappop(min_heap)
                while not memo[val]:
                    if not min_heap:
                        break
                    val = heapq.heappop(min_heap)
                else:
                    memo[val] -= 1
            else:
                if not max_heap:
                    continue
                val = -1*heapq.heappop(max_heap)
                while not memo[val]:
                    if not max_heap:
                        break
                    val = -1*heapq.heappop(max_heap)
                else:
                    memo[val] -= 1
    max_val = None
    if max_heap:
        max_val = -1*heapq.heappop(max_heap)
        while not memo[max_val]:
            if not max_heap:
                max_val = None
                break
            max_val = -1*heapq.heappop(max_heap)
        else:
            memo[max_val] -= 1
    min_val = None
    if min_heap:
        min_val = heapq.heappop(min_heap)
        while not memo[min_val]:
            if not min_heap:
                min_val = None
                break
            min_val = heapq.heappop(min_heap)
        else:
            memo[min_val] -= 1

    if max_val == None and min_val == None:
        print('EMPTY')
    elif min_val == None:
        print(max_val, max_val)
    elif max_val == None:
        print(min_val, min_val)
    else:
        print(max_val, min_val)