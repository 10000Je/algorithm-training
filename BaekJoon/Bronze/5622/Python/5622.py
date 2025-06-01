mapping = {}
mapping.update({'A': 3, 'B': 3, 'C': 3})
mapping.update({'D': 4, 'E': 4, 'F': 4})
mapping.update({'G': 5, 'H': 5, 'I': 5})
mapping.update({'J': 6, 'K': 6, 'L': 6})
mapping.update({'M': 7, 'N': 7, 'O': 7})
mapping.update({'P': 8, 'Q': 8, 'R': 8, 'S': 8})
mapping.update({'T': 9, 'U': 9, 'V': 9})
mapping.update({'W': 10, 'X': 10, 'Y': 10, 'Z': 10})

word = input()
time = 0
for char in word:
    time += mapping[char]
print(time)
