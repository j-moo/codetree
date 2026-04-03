N = int(input())

# 소수라고 가정
satisfied = 'P'
for i in range(2, N):
    if N % i == 0:
        satisfied = 'C'

print(satisfied)