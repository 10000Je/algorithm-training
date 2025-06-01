n = int(input())
seat = input()
print(min(seat.count('LL')+seat.count('S')+1, n))
        