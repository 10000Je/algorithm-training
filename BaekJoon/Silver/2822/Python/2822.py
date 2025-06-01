points = []
for i in range(1, 9):
    point = int(input())
    points.append((i, point))
points.sort(key=lambda x: x[1])
print(sum(map(lambda x: x[1], points[-1:-6:-1])))
print(*map(lambda x:x[0], sorted(points[-1:-6:-1])), sep=' ')