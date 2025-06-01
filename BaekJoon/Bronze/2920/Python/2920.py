import sys

def getStatus(array):
    if array[0] == 1:
        for i in range(0, len(array)):
            if i+1 != array[i]:
                return 'mixed'
        return 'ascending'
    elif array[0] == 8:
        for i in range(0, len(array)):
            if len(array)-i != array[i]:
                return 'mixed'
        return 'descending'
    else:
        return 'mixed'

arr1 = list(map(int, sys.stdin.readline().split()))
print(getStatus(arr1))
