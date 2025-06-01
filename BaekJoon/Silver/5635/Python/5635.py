import sys

class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    name, day, month, year = sys.stdin.readline().split()
    day, month, year = map(int, [day, month, year])
    person = Person(name, year, month, day)
    data.append(person)
data.sort(key=lambda x: (x.year, x.month, x.day))
print(data[-1].name, data[0].name, sep='\n')

