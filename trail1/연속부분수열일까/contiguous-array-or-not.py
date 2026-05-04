A, B = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

answer = 'No'
for i in range(A - B + 1):
    cnt = 0
    for j in range(B):
        if a_arr[i + j] == b_arr[j]:
            cnt += 1
    if cnt == B:
        answer = 'Yes'

print(answer)