import sys

class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

n = int(sys.stdin.readline())
students = []
for _ in range(n):
    name, korean, english, math = sys.stdin.readline().split()
    korean, english, math = map(int, (korean, english, math))
    students.append(Student(name, korean, english, math))

students.sort(key=lambda x:(x.korean*(-1), x.english, x.math*(-1), x.name))
print(*map(lambda x:x.name, students), sep='\n')