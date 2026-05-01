# 정수의 개수 n을 입력받습니다.
n = int(input())

# 배열을 구현하여 주어진 수를 입력받습니다.
arr = list(map(int, input().split()))
	
# 입력받은 수들을 거꾸로 보면서 짝수인 값만 출력합니다.
for i in range(n-1, -1, -1):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")
