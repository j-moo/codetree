S, Q = input().split()
S = list(S)
Q = int(Q)

for _ in range(Q):
    a, b, c = input().split()
    if int(a) == 1:
        index_1 = int(b) - 1
        index_2 = int(c) - 1
        s_1, s_2 = S[index_1], S[index_2]
        S[index_1] = s_2
        S[index_2] = s_1
        print(''.join(S))
    else:
        for i in range(len(S)):
            if S[i] == b:
                S[i] = c
        print(''.join(S))