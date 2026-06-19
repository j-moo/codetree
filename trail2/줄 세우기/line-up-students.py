class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())

students = []

for num in range(1, n + 1):
    height, weight = map(int, input().split())
    
    students.append(Student(height, weight, num))

students.sort(key=lambda x: (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)