# 정수의 개수 입력
N = int(input())

# 정수를 리스트로 저장
arr = list(map(int, input().split()))

# 정수 리스트를 뒤에서부터 순회하며 짝수이면 해당 정수를 출력
for i in range(len(arr) - 1, -1, -1):
    # 2로 나눈 나머지가 0 이라면 짝수
    if arr[i] % 2 == 0:
        print(arr[i], end = ' ')