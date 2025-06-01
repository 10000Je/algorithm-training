# no. 1987: 알파벳 (Gold IV)

# 세로 R칸 가로 C칸으로 된 표 모양의 보드가 있다.
# 말은 상하좌우로 인접한 칸으로 이동할 수 있다.
# 보드의 각 칸에는 알파벳이 적혀있는데, 말은 한가지 규칙 아래에서 움직인다.
# "같은 알파벳을 두번 밟을 수 없다."
# 위 조건을 만족하며 말이 이동할때 말은 최대 몇칸을 지나갈 수 있을까?

# 백트래킹 문제로 보인다.
# 말은 이동할 때 해당 칸에 있는 알파벳이 이미 지나온 알파벳인지 확인해야 한다.
# 이는 HashSet 자료형을 사용하는 것이 좋을 듯 하다. 룩업 -> O(1)
# 어차피 알파벳은 26개밖에 없으므로 최대 깊이는 26이 될것이다.

# 처음에는 다음 재귀로 갈때마다 알파벳 set을 복사시켜 주었는데
# 생각해보니 복사할 필요가 없다. dfs는 더이상 갈 이웃이 없는 동안 계속 깊이 들어가므로
# 더이상 갈 이웃이 없다 -> 루프문이 종료되었다. -> 루프문이 종료될때 
# 알파벳 set에 현재 정점의 알파벳을 제거하면 된다.
# 그럼 해당 재귀 호출이 끝나고 이전 재귀로 back 할때
# 알파벳 set에는 해당 재귀호출 까지의 알파벳이 저장되어 있을 것이다.

# 처음에는 알파벳과 루트 2개의 set으로 이동이 가능한 정점을 구하려고 했는데
# 생각해보니 알파벳만 기록해둬도 상관이 없다 왜냐면 루트의 목적은 중복이동을 
# 막기 위한 것이고, 이미 지나온 정점은 알파벳으로 기록되어 있으므로 하나만 있어도 된다.

# 계속 끝나지않는 시간초과 공세에 지쳐 쓰려저 갈때쯤 인터넷으로 이에 대한 최적화
# 방법이 없을까 찾고 있었다.
# 결론은 해쉬총돌(Hash Collision)을 고려해야 한다는 것이였다.
# 해쉬충돌은 한 객체에 대한 해쉬값이 동일하여 충돌을 일으키는 현상으로
# 해쉬충돌을 해결하는 과정(새로운 배열만들고 참조 등)으로 룩업시간이 증가하는 현상이다.
# 이를 해결하는 방법은 단순히 리스트를 쓰는 방법도 있겠지만
# 알파벳을 아스키코드로 바꿔 셋에 넣으면 해쉬충돌을 피하고 속도에 이점을 얻을 수 있어
# 이를 활용하였다.

# 알게된점.
# 백트래킹할때 새로운 자료구조 생성할 필요 없음 (모든 경우가 그런건 아님)
# hash기반 자료구조들은 숫자를 저장하는 것이 문자를 저장하는 것보다 더 빠름
# 튜플이 리스트보다 빠름

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = tuple(tuple(map(ord, input().rstrip())) for _ in range(r))

def dfs(start=(0, 0), alphabets={board[0][0]}, max_depth=[1]):
    row, col = start
    near_cells = (
        (row, col+1), (row+1, col), (row, col-1), (row-1, col)
    )
    for near_cell in near_cells:
        n_row, n_col = near_cell
        if not (0 <= n_row < r and 0 <= n_col < c):
            continue
        if board[n_row][n_col] in alphabets:
            continue
        alphabets.add(board[n_row][n_col])
        dfs(near_cell, alphabets, max_depth)
    max_depth[0] = max(max_depth[0], len(alphabets))
    alphabets.remove(board[row][col])
    return max_depth[0]

max_depth = dfs()
print(max_depth)