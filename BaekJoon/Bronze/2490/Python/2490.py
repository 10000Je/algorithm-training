result = ['D', 'C', 'B', 'A', 'E']
for _ in range(3):
    cnt = list(map(int, input().split())).count(1)
    print(result[cnt])