s_1, S_2 = input().split()

if len(s_1) > len(S_2):
    print(s_1, len(s_1))
elif len(s_1) < len(S_2):
    print(S_2, len(S_2))
else:
    print('same')
    