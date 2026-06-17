n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

answer = 'Yes'
for idx in range(n):
    if A[idx] != B[idx]:
        answer = 'No'
        break

print(answer)