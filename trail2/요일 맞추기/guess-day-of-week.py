m1, d1, m2, d2 = map(int, input().split())

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

start = sum(month[:m1]) + d1
end = sum(month[:m2]) + d2

answer = (end - start) % 7
print(days[answer])