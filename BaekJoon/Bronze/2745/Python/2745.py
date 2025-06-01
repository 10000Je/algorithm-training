import sys

n, b = sys.stdin.readline().split()
b = int(b)
hashMap = dict(zip('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(0, 36)))
result = 0
for digit, each_number in enumerate(n):
    result += hashMap[each_number] * (b ** (len(n)-1-digit))
print(result)