n, m = map(int, input().split())
castle = [[cell for cell in input().rstrip()] for _ in range(n)]
missed_row = []
for row in range(n):
    for col in range(m):
        if castle[row][col] == 'X':
            break
    else:
        missed_row.append(row)
missed_col = []
for col in range(m):
    for row in range(n):
        if castle[row][col] == 'X':
            break
    else:
        missed_col.append(col)
print(max(len(missed_row), len(missed_col)))