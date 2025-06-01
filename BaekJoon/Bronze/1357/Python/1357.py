x, y = input().split()
print(int(f'{int(x[::-1])+int(y[::-1])}'[::-1]))