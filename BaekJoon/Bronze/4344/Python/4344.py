import sys

c = int(sys.stdin.readline())
for _ in range(c):
    r_data = [num for num in map(int, sys.stdin.readline().split())]
    avg = sum(r_data[1:])/(len(r_data)-1)
    cnt = 0
    for student in r_data[1:]:
        if student > avg:
            cnt += 1
    print(f'{(cnt/(len(r_data)-1))*100:.3f}%')