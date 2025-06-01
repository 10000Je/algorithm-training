import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = []
for i in range(0, n):
    ground.append(tuple(map(int, sys.stdin.readline().split())))
field_block = sum(map(sum, ground))
min_height = min(map(min, ground))
max_height = max(map(max, ground))

min_time = None
max_height_with_min_time = None
for height in range(min_height, max_height+1):
    needed_block = n*m*height
    if field_block + b < n*m*height:
        continue
    current_time = 0
    for row in ground:
        for cell in row:
            if cell >= height:
                difference = cell-height
                current_time += 2*difference
            else:
                difference = height-cell
                current_time += difference
    if min_time == None:
        min_time = current_time
        max_height_with_min_time = height
    else:
        if current_time < min_time:
            min_time = current_time
            max_height_with_min_time = height
        elif current_time == min_time:
            if height > max_height_with_min_time:
                max_height_with_min_time = height
print(min_time, max_height_with_min_time, sep=' ')