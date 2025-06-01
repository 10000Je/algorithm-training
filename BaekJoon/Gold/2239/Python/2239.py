# no. 2239: 스도쿠 (Gold IV)
# 빈칸들의 위치를 배열로 저장
# (r1, c1), (r2, c2)...(rn, cn) 이 zero 배열의 원소라고 해보자
# 완전탐색으로 depth가 증가하면, zero 배열의 인덱스도 증가시켜,
# "현재 채우려고 하고 있는 빈칸"을 변경한다
# depth가 n(빈칸의 개수)과 같아지면, 더이상 채울 빈칸이 없다는 의미, 즉 스도쿠를 다 풀었다는 의미이다

# 사전순으로 가장 앞에오는 스도쿠 정답을 출력하라는 말의 의미를 잘 파악해야한다
# 결국 백트래킹으로 앞의 빈칸들부터 가능한 숫자들중 작은 숫자부터 먼저 시도한다면
# 처음으로 나온 답이 결국 사전순으로 가장 작을 수 밖에 없다
# 따라서, 답이 완성되면 백트래킹을 멈추도록 하는 것이 좋다

# 체감 난이도: Gold II
# 백트래킹 자체는 어려운 것이 아니나, 최적화 과정이 항상 어려운 것 같다
# 아이디어는 단순하나, 코드 구현난이도가 쉽지 않은 편

from sys import stdin
input = stdin.readline

board = [list(map(int, input().rstrip())) for _ in range(9)]
zero = [(r, c) for r in range(9) for c in range(9) if board[r][c]==0]

def brute_force(depth=0, result=None):
    if result == None: result = [None]
    if result[0] != None:
        return result[0]
    if depth == len(zero):
        result[0] = [arr.copy() for arr in board]
        return result[0]
    r, c = zero[depth]
    exist_num = set()
    for i in range(9):
        if board[r][i]:
            exist_num.add(board[r][i])
    for i in range(9):
        if board[i][c]:
            exist_num.add(board[i][c])
    r2 = r - (r%3)
    c2 = c - (c%3)
    for i in range(r2, r2+3):
        for j in range(c2, c2+3):
            if board[i][j]:
                exist_num.add(board[i][j])
    for n in range(1, 10):
        if n in exist_num:
            continue
        board[r][c] = n
        brute_force(depth+1, result)
        board[r][c] = 0
    return result[0]
            
result = brute_force()
for arr in result:
    print(*arr, sep='')