N = int(input())    # 원소의 개수

# 입력받을 원소를 리스트로 저장
arr = list(map(int, input().split()))

# 각 원소를 제곱하여 출력
for i in range(N):
    print(arr[i] ** 2, end=' ')