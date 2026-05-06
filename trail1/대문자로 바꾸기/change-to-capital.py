matrix = [list(input().split()) for _ in range(5)]

for arr in matrix:
    for elem in arr:
        elem = elem.upper()
        print(elem, end=' ')
    print()