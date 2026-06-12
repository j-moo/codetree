n = int(input())

def print_star(n):
    for i in range(n):
        print('*', end=' ')
    print()

def count_num(n):
    if n == 0:
        return

    
    print_star(n)
    count_num(n - 1)
    print_star(n)

count_num(n)