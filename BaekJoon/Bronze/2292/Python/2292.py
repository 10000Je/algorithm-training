import sys

def getMinimumDistance(n):
    if n == 1:
        return 1
    else:
        room = 2
        distance = 2
        while room <= n:
            room += 6 * (distance-1)
            distance += 1
        return distance-1
                
n = int(sys.stdin.readline())
print(getMinimumDistance(n))
