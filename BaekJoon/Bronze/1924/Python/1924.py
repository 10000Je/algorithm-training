months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
x, y = map(int, input().split())
days = -1
for i in range(x):
    days += months[i]
days += y
print(weeks[days%7])
