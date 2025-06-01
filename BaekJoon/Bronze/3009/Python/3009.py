point = {tuple(map(int, input().split())) for _ in range(3)}
x_range = [min(point, key=lambda x: x[0])[0], max(point, key=lambda x: x[0])[0]]
y_range = [min(point, key=lambda x: x[1])[1], max(point, key=lambda x: x[1])[1]]
for x in x_range:
    for y in y_range:
        if (x, y) not in point:
            print(x, y)
            break
    else:
        continue
    break
