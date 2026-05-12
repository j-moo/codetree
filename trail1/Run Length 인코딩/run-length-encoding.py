string = input()
answer = ''

cnt = 1  # 첫 번째 문자부터 카운트
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        cnt += 1
    else:
        answer += string[i] + str(cnt)
        cnt = 1  # 새로운 문자 시작

# 마지막 문자 처리
answer += string[-1] + str(cnt)

print(len(answer))
print(answer)