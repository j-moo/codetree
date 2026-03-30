# 두 정수 입력받기
A, B = map(int, input().split())

# 큰 수에서 작은 수를 뺀 값을 출력
if A > B:
    print(A - B)
elif A < B:
    print(B - A)
else:
    print(A - B)