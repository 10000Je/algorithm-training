import sys

n, k = map(int, sys.stdin.readline().split())
points = [point for point in map(int, sys.stdin.readline().split())]
points.sort()
print(points[-1*k])