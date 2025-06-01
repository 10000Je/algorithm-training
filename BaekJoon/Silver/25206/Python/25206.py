grade_table = {
    'A0': 4.0, 'A+': 4.5,
    'B0': 3.0, 'B+': 3.5,
    'C0': 2.0, 'C+': 2.5,
    'D0': 1.0, 'D+': 1.5,
    'F': 0.0
    }
total_scores = []
scores = []
for _ in range(20):
    name, score, grade = input().split()
    if grade != 'P':
        scores.append(float(score))
        total_scores.append(float(score)*grade_table[grade])
print(sum(total_scores)/sum(scores))