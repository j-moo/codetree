class Student:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

n = int(input())

students = []

for _ in range(n):
    name, a, b, c = input().split()
    a, b, c = map(int, (a, b, c))

    students.append(Student(name, a, b, c))

students.sort(key=lambda x: (x.s1 + x.s2 + x.s3))

for student in students:
    print(student.name, student.s1, student.s2, student.s3)