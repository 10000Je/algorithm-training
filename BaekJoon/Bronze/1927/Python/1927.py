import sys

# Python의 heapq 모듈을 사용하면 훨씬 간편하고 빠르다.
# 하지만 여기선 구현연습을 위해 직접 Heap 추상 데이터 타입을 구현하였다.
class Heap:
    def __init__(self):
        self.heap = []
    
    def push(self, value):
        heap = self.heap
        heap.append(value)
        cur_index = len(heap) - 1
        while cur_index > 0 and heap[(cur_index-1)//2] > heap[cur_index]:
            heap[(cur_index-1)//2], heap[cur_index] = heap[cur_index], heap[(cur_index-1)//2]
            cur_index = (cur_index-1) // 2
        return cur_index

    def pop(self):
        heap = self.heap
        if not heap:
            return 0
        val = heap[0]
        if len(heap) == 1:
            return heap.pop()
        heap[0] = heap.pop()
        cur_index = 0
        child_index = self.getSmallerChild(cur_index)
        while child_index:
            heap[cur_index], heap[child_index] = heap[child_index], heap[cur_index]
            cur_index = child_index
            child_index = self.getSmallerChild(cur_index)
        return val

    def getSmallerChild(self, index):
        heap = self.heap
        heap_length = len(heap)
        if index * 2 + 1 >= heap_length and index * 2 + 2 >= heap_length:
            return None
        elif index * 2 + 1 >= heap_length:
            if heap[index*2+2] < heap[index]:
                return index*2+2
            else:
                return None
        elif index * 2 + 2 >= heap_length:
            if heap[index*2+1] < heap[index]:
                return index*2+1
            else:
                return None
        else:
            smaller_child = index*2+1 if heap[index*2+1] < heap[index*2+2] else index*2+2
            if heap[smaller_child] < heap[index]:
                return smaller_child
            else:
                return None

n = int(sys.stdin.readline())
heap1 = Heap()
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heap1.pop())
    else:
        heap1.push(x)
