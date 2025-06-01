# no. 9328: 열쇠 (Gold I)
# dfs로 접근
# 문을 발견했을 때 어떻게 대처하느냐가 관건
# -> 현재 열쇠를 가지고 있다면 -> 문을 열고 dfs를 계속 진행
# -> 현재 열쇠를 가지고 있지 않다면 -> 해당 문의 번호와 위치를 기억하고, 계속 dfs 수행
# 열쇠를 발견시,
# 만약 지금까지 발견하지 못한 열쇠라면, 이 열쇠를 줍고 "기억해둔" 문의 번호와 위치
# 를 이용해, 해당 문들의 위치에서 dfs를 시작하게함
# 이미 발견한 열쇠라면, 그냥 줍고 계속 dfs

# 16% 틀렸습니다. -> 이 문제는 특이하게, 입구에서 입구사이로는 건물 외벽을 통해
# 이동할 수 있기 때문에, r=0, h-1, c=0, w-1 일때 이웃정점을 다르게 설정해줘야한다
# 하지만, 문이 외벽에 있는 경우, 이 문이 열리면 이것도 이제 이웃정점에 포함시켜줘야
# 하기 때문에 이를 고려하지 못하여서 틀렸습니다...
# 간단하게 가장자리에 있는 블럭에는 접근가능하니까, .으로 패딩을 둘러싸면 문제가
# 다소 단순해짐.

# 체감 난이도: Platinum V
# 구현 너무 빡셌고, 사고의 전환도 필요하고, 반례 케이스 잘 다뤄야하고
# 실수하면 존나 힘들고, 입출력 다루는것도 쉽지 않은 총체적 난국 문제
# 문제 접근이라도 성공했다는 것에 만족해야하나..
# bfs 문제긴 한데, dfs로도 풀 수 있다.

from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    grid = [['.' for _ in range(w+2)]]
    for _ in range(h):
        arr = ['.'] + list(input().rstrip()) + ['.']
        grid.append(arr)
    grid.append(['.' for _ in range(w+2)])
    h += 2; w += 2
    key_input = input().rstrip()
    if key_input == '0':
        keys = set()
    else:
        keys = {char for char in key_input}
    
    def is_door(r, c):
        if ord('A') <= ord(grid[r][c]) <= ord('Z'):
            return True
        else:
            return False
    
    def is_key(r, c):
        if ord('a') <= ord(grid[r][c]) <= ord('z'):
            return True
        else:
            return False

    def dfs(cur_loc, visited=None, doors=None, cnt=None):
        if visited == None: visited = {cur_loc}
        if doors == None: doors = {chr(i): [] for i in range(ord('A'), ord('Z')+1)}
        if cnt == None: cnt = [0]
        row, col = cur_loc

        if is_key(row, col) and grid[row][col] not in keys:
            keys.add(grid[row][col])
            for door_loc in doors[grid[row][col].upper()]:
                dfs(door_loc, visited, doors, cnt)

        near_locs = {(row-1, col), (row, col+1), (row+1, col), (row, col-1)}
            
        for near_loc in near_locs:
            row_n, col_n = near_loc
            if not ((0 <= row_n < h) and (0 <= col_n < w)): continue
            if grid[row_n][col_n] == '*': continue
            if near_loc in visited: continue
            visited.add(near_loc)
            if is_door(row_n, col_n):
                if grid[row_n][col_n].lower() not in keys:
                    doors[grid[row_n][col_n]].append((row_n, col_n))
                    continue
            if grid[row_n][col_n] == '$':
                cnt[0] += 1
            dfs(near_loc, visited, doors, cnt)

        return cnt[0]

    cnt = dfs((0, 0))
    print(cnt)
