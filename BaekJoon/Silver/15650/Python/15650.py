import sys

def get_sequences(n, depth, cur_sequence='', sequences=[]):
    if depth == 0:
        sequences.append(cur_sequence)
    for i in range(1, n+1):
        if str(i) in cur_sequence:
            continue
        if cur_sequence and int(cur_sequence[-1]) > i:
            continue
        get_sequences(n, depth-1, cur_sequence+str(i), sequences)
    return sequences

n, m = map(int, sys.stdin.readline().split())
sequences = get_sequences(n, m)
sequences.sort()
for sequence in sequences:
    print(*[char for char in sequence])