def alpha(string):
    pre = ''
    for elem in string:
        if pre == '':
            pre = elem
        
        if elem != pre:
            return True
    return False

A = input()

if alpha(A):
    print('Yes')
else:
    print('No')