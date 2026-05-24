def solve(n1, n2, arr_a, arr_b):
    for i in range(n1 - n2 + 1):
        if arr_a[i:i+n2] == arr_b:
            print("Yes")
            return

    print("No")


n1, n2 = map(int, input().split())

arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

solve(n1, n2, arr_a, arr_b)