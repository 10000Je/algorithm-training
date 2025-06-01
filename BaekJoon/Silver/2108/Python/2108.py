import sys

n = int(sys.stdin.readline())
arr1 = []
memo = {}
for i in range(0, n):
    num = int(sys.stdin.readline())
    if num not in memo:
        memo[num] = 1
    else:
        memo[num] += 1
    arr1.append(num)
arr1.sort()

sum = 0
for val in arr1:
    sum += val

average = round(sum / n)
median = arr1[(0+len(arr1)-1)//2]
range = arr1[-1] - arr1[0]
mode_keys = []
mode_max = 0
for key in memo:
    if memo[key] > mode_max:
        mode_keys = []
        mode_max = memo[key]
        mode_keys.append(key)
    elif memo[key] == mode_max:
        mode_keys.append(key)
    else:
        pass
mode_keys.sort()

mode = mode_keys[0] if len(mode_keys) == 1 else mode_keys[1]
print(average, median, mode, range, sep='\n')
