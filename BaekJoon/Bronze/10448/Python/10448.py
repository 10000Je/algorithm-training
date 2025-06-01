import sys

tri_nums = []
n = i = 1
while n <= 1000:
    tri_nums.append(n)
    i += 1
    n = (i*(i+1))//2

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    for i in tri_nums:
        for j in tri_nums:
            for k in tri_nums:
                if i+j+k == n:
                    print(1)
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(0)