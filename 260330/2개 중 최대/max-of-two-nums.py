# 두 정수 입력받기
A, B = map(int, input().split())

# 최댓값을 출력
print(A if A > B else B)