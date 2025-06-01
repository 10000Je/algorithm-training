n = int(input())
heights = [num for num in map(int, input().split())]
last_height = 1
max_kill = 0
cur_kill = 0
for height in heights:
    if height > last_height:
        max_kill = max(max_kill, cur_kill)
        last_height = height
        cur_kill = 0
    else:
        cur_kill += 1
max_kill = max(max_kill, cur_kill)
print(max_kill)