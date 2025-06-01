import math

m = int(input())
n = int(input())
nums = [i**2 for i in range(math.ceil(m**0.5), int(n**0.5)+1)]
if nums:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)