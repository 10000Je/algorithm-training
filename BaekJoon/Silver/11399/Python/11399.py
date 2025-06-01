import sys

'''
* recursion algorithm (excluded due to recursion depth)
def prefix_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return sum(array) + prefix_sum(array[:-1])
'''

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
sum = 0
for i in range(len(p)):
    for j in range(0, i+1):
        sum += p[j]
print(sum)