# 5개의 문자열을 리스트로 저장
fruit = ['apple', 'banana', 'grape', 'blueberry', 'orange']

# 영문자 하나를 입력 받기
alpha = input()

# 문자열 리스트를 순회하며 영문자가 해당 문제의 3, 4번째 문자와 일치하면
# 카운트 +1
# 해당 문자열 출력

# 조건을 만족했을 때 개수를 출력할 변수
cnt = 0

for i in fruit:
    if i[2] == alpha or i[3] == alpha:
        cnt += 1
        print(i)

print(cnt)