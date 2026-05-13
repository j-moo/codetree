a = input()
b = input()

a_len = len(a)
b_len = len(b)

cnt = 0
for i in range(a_len - b_len + 1):
    is_match = True
    for j in range(b_len):
        if a[i+j] != b[j]:
            is_match = False
            break
    
    if is_match:
        cnt += 1

print(cnt)