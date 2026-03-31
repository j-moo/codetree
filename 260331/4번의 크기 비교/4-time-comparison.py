# A 입력받기
A = int(input())
# B, C, D, E 입력받기
B, C, D, E = map(int, input().split())

# A와 비교 연산자를 통해 판별
print(1 if A > B else 0)
print(1 if A > C else 0)
print(1 if A > D else 0)
print(1 if A > E else 0)