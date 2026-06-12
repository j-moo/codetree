n = int(input())

def print_number(num):
    if num == n + 1:
        print()
        return

    print(num, end=' ')
    print_number(num + 1)
    print(num, end=' ')

print_number(1)