n = int(input())

def n_queen(row, pos, results=[]):
    if row == n:
        results.append(pos.copy())
        return
    for i in range(n):
        for j in range(row):
            if i == pos[j] or abs(row-j) == abs(i-pos[j]):
                break
        else:
            pos[row] = i
            n_queen(row+1, pos, results)
    pos[row] = -1
    return results

pos = [-1 for _ in range(n)]
result = n_queen(0, pos)
print(len(result))