# no. 9466: 텀 프로젝트 (Gold III)
# 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하라
# 팀이란건 하나의 원형사이클을 이루고 있는 학생들을 의미한다
# 이 때 원형사이클은 자기가 자신을 연결하고 있는 경우도 가능하다
# 그러면, 팀이 아닌 인원은 아래의 조건을 만족한다
# -> 자기자신이 아닌 다른학생을 선택해야 하며, 
# 그 연결의 끝이 본인이 아닌 경우

# 팀인 경우는 아래의 조건들 중 하나를 만족한다
# 자기자신을 연결하고 있는 경우(이러한 경우 본인 혼자가 팀이된다)
# 타인을 연결하고 그 끝이 자신으로 되돌아 오는 경우(이런경우 사이클 내에 있는 사람들이 팀이된다)

# 매번 연결리스트식 참조를 통해 사이클을 발견할때마다 (팀을 발견할때마다)
# 팀인 학생을 제외한 나머지 학생들을 -> 속하지 않는 학생 set에 넣어줌
# stack에 푸시되어 있는 학생들은 전부다 배열에서 제거해줌

# 후기 -> 체감 난이도 (Gold II)
# 나는 집합을 이용한 방식으로 풀이하였는데, 알고리즘 힌트를 보니
# dfs 로도 풀이할 수 있었다.
# 순환 사이클을 이용한다는 아이디어 자체는 동일하여서 정답으로 접근이 가능했고,
# dfs 풀이는, dfs를 이용하여 팀을 이루는 인원을 탐색하여서
# 전체에서 팀을 이루는 인원들의 수를 빼는 해법이였다
# dfs 풀이도 참고하면 후에 도움이 될 듯 하다.
# 힌트를 전혀 안보고 푸니, 신박한 풀이로 계속 풀게되는 느낌이다...
# 기분은 좋은데 ㅈ뺑이를 치고있다는 느낌을 지울 수가..

from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums = (0,) + tuple(map(int, input().split()))
    students = {i for i in range(1, n+1)}
    alone_students = set()
    while students:
        stack = []
        pushed_students = set()
        cycle_start = None

        cur_student = students.pop()
        students.add(cur_student)
        while True:
            if cur_student in pushed_students:
                cycle_start = cur_student
                cur_student = stack.pop()
                while cur_student != cycle_start:
                    students.remove(cur_student)
                    cur_student = stack.pop()
                students.remove(cycle_start)
                while stack:
                    cur_student = stack.pop()
                    alone_students.add(cur_student)
                    students.remove(cur_student)
                break

            stack.append(cur_student)
            pushed_students.add(cur_student)
            cur_student = nums[cur_student]

            if cur_student not in students:
                while stack:
                    cur_student = stack.pop()
                    alone_students.add(cur_student)
                    students.remove(cur_student)
                break
    print(len(alone_students))