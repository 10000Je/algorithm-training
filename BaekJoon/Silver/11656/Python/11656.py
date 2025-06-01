s = input()
tails = [s[i:] for i in range(len(s))]
tails.sort()
print(*tails, sep='\n')
