import sys

def max_point(n, points, memo={}):
    if n == 0:
        return points[0]
    if n == 1:
        return points[0] + points[1]
    if n == 2:
        return max(points[1] + points[2], points[0] + points[2])
    if n-2 not in memo:
        memo[n-2] = max_point(n-2, points, memo)
    if n-3 not in memo:
        memo[n-3] = max_point(n-3, points, memo)
    if n not in memo:
        memo[n] = max(memo[n-3] + points[n-1] + points[n], memo[n-2] + points[n])
    return memo[n]

n = int(sys.stdin.readline())
points = [int(sys.stdin.readline()) for i in range(n)]
print(max_point(n-1, points))