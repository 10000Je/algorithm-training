import sys
n = sys.stdin.readline().rstrip()
hashMap = dict(zip('0123456789ABCDEF', range(0, 16)))

result = 0
for idx, each_number in enumerate(n):
    result += hashMap[each_number] * (16 ** (len(n)-idx-1))
print(result)