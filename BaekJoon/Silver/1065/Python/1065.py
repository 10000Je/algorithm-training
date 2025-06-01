import sys

def isHansu(n):
    str1 = str(n)
    last_distance = None
    for i in range(0, len(str1)-1):
        if last_distance != None and int(str1[i]) - int(str1[i+1]) != last_distance:
            return False
        last_distance = int(str1[i]) - int(str1[i+1])
    return True

n = int(sys.stdin.readline())
nums = [i for i in range(1, n+1) if isHansu(i)]
print(len(nums))