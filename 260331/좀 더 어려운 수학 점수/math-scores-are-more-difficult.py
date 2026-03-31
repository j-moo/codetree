# 각 학생별 점수 입력받기 
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A[0] > B[0]:
    print(A)
elif A[0] < B[0]:
    print(B)
else:
    if A[1] > B[1]:
        print(A)
    elif A[1] < B[1]:
        print(B)

        