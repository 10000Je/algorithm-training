n = int(input())
nums = [num for num in map(int, input().split())]
print(max(nums)*min(nums))