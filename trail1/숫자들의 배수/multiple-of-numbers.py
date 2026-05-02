N = int(input())

cnt = 1
five_cnt = 0
while five_cnt < 2:
    elem = N * cnt
    print(elem, end=' ')

    if elem % 5 == 0:
        five_cnt += 1
    
    cnt += 1