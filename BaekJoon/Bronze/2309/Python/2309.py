heights = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(9):
        new_heights = [heights[idx] for idx in range(9) if idx != i and idx != j and i != j]
        if sum(new_heights) == 100:
            new_heights.sort()
            print(*new_heights, sep='\n')
            break
    else:
        continue
    break