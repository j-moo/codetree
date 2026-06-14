n = int(input())
arr = list(map(int, input().split()))

num_max = 0
def f(n):
    global num_max
    if n == 0:
        return

    if num_max < arr[n - 1]:
        num_max = arr[n - 1]
    
    f(n - 1)

f(n)
print(num_max)