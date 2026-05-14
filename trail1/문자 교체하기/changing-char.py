s_1, s_2 = input().split()
s_1 = list(s_1)
s_2 = list(s_2)

s_2[0] = s_1[0]
s_2[1] = s_1[1]

print(''.join(s_2))