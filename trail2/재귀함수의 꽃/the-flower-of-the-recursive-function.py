N = int(input())

def print_number(num):
    if num == 0:
        return

    print(num, end=' ')
    print_number(num - 1)
    print(num, end=' ')

print_number(N)