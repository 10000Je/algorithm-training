n, m = map(int, input().split())

def get_sequences(n, m, cur_sequence='', sequences=[]):
    if m == 0:
        sequences.append(cur_sequence)
        return
    for cur_num in range(1, n+1):
        if not cur_sequence or cur_num >= int(cur_sequence[-1]):
            get_sequences(n, m-1, cur_sequence + str(cur_num), sequences)
    return sequences

sequences = get_sequences(n, m)
sequences.sort()
for sequence in sequences:
    print(*list(sequence))