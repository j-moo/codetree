# 입력 텍스트를 나누어 리스트로 저장
text = list(input())

# 텍스트 2번 째 원소를 'a'로 변경
text[1] = 'a'

# 텍스트 뒤에서 두 번째 원소를 'a'로 변경
text[-2] = 'a'

# 전체 텍스트 출력
print(''.join(text))
