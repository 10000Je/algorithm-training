word = input()
divided_words = []
for i in range(1, len(word)):
    for j in range(i+1, len(word)):
        head = word[:i]
        body = word[i:j]
        tail = word[j:]
        divided_words.append(head[::-1]+body[::-1]+tail[::-1])
divided_words.sort()
print(divided_words[0])