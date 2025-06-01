import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for i in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

current_coin_idx = len(coins)-1
coin_count = k // coins[current_coin_idx]
current_total = coins[current_coin_idx] * coin_count
while current_total != k:
    while current_total < k:
        coin_count += 1
        current_total += coins[current_coin_idx]
    if current_total == k:
        break
    coin_count -= 1
    current_total -= coins[current_coin_idx]
    current_coin_idx -= 1
print(coin_count)