# no. 1644: 소수의 연속합 (Gold III)
# 한 숫자가 주어졌을때 이 수를 연속된 소수의 합으로 나타낼 수 있는 
# 경우의 수를 출력하는 문제
# 에라토스테네스의 체를 이용하여 O(N)시간안에 연속된 소수 수열을 구하고,
# 투 포인터를 이용하여 경우의 수를 구하면 O(N)시간안에 문제를 풀 수 있다.

# 어떠한 숫자가 소수의 합으로 이루어져있다고 가정할때, 해당하는 각 소수는 숫자보다
# 클 수 없으므로 구해야할 연속된 소수의 범위는 1부터 n까지 이다.

# 후기:
# 체감 난이도: Gold II
# 풀이시간은 짧았으나, 에라토스테네스의 체를 모르면 문제를 풀기 어렵고
# 이를 투포인터로 접근하겠다는 아이디어를 떠올리는 것이 사실 쉽지만은 않다
# (물론 내가 풀때는 1분만에 떠올리긴 했는데)
# 반례케이스로 소수가 하나도 없는 경우가 있어서 이것때문에 한번 틀렸다.
# 에라토스테네스의 체의 강력함을 알 수 있었던 문제

n = int(input())

nums = [i for i in range(n+1)]
nums[1] = 0
for i in range(2, n+1):
    if nums[i]:
        j = i+i
        while j <= n:
            nums[j] = 0
            j += i

prime_nums = [i for i in range(n+1) if nums[i]]
len_p = len(prime_nums)

i = j = 0
cur_sum = prime_nums[0] if prime_nums else 0
cnt = 0
while True:
    if cur_sum == n:
        cnt += 1
        i += 1
        cur_sum -= prime_nums[i-1]
        continue
    if cur_sum < n:
        j += 1
        if j >= len_p: break
        cur_sum += prime_nums[j]
        continue
    if cur_sum > n:
        i += 1
        cur_sum -= prime_nums[i-1]

print(cnt)