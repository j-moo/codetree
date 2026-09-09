n, m, k = map(int, input().split())
students = [0] * (n + 1)

answer = -1
for _ in range(m):
    idx = int(input())
    students[idx] += 1
    
    if students[idx] == k:
        answer = idx
        break

print(answer)