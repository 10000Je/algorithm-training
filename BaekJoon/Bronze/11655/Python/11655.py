s = input()
new_s = []
for char in s:
    if ord('A') <= ord(char) <= ord('Z'):
        new_s.append(chr((ord(char)-ord('A')+13)%26+ord('A')))
    elif ord('a') <= ord(char) <= ord('z'):
        new_s.append(chr((ord(char)-ord('a')+13)%26+ord('a')))
    else:
        new_s.append(char)
print(*new_s, sep='')