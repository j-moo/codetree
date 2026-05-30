def modify(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    return a, b

a, b = map(int, input().split())

# Please write your code here.
a, b = modify(a, b)
print(a, b)