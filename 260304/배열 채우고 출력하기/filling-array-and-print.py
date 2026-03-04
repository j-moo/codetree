# 문자 10개를 입력받아 리스트로 저장
arr = list(input().split())

# 배열을 역순으로 변경
arr.reverse()

# 10번 반복하여 출력
for i in range(10):
    print(arr[i], end='')