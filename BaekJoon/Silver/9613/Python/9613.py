import sys

t = int(sys.stdin.readline())
for _ in range(t):
    nums = [num for num in map(int, sys.stdin.readline().split())]
    n = nums.pop(0)
    gcds = []
    for i in range(n):
        for j in range(i+1, n):
            a = max(nums[i], nums[j])
            b = min(nums[i], nums[j])
            while b:
                r = a % b
                a = b
                b = r
            gcds.append(a)
    print(sum(gcds))