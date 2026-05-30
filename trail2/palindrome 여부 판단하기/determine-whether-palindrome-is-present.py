def reverse_string(A):
    string = A[::-1]
    return string

A = input()

if A == reverse_string(A):
    print('Yes')
else:
    print('No')