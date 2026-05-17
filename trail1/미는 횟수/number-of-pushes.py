A = input()
B = input()

answer = -1

for i in range(1, len(A) + 1):
    # 오른쪽으로 한 칸 밀기
    A = A[-1] + A[:-1]

    if A == B:
        answer = i
        break

print(answer)