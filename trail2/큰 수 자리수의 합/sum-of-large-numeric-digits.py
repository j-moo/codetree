a, b, c = map(int, input().split())

def f(n):
    if n < 10:
        return n
    return f(n // 10) + (n % 10)


def solve(a, b, c):
    answer = a * b * c

    answer = f(answer)

    return answer

print(solve(a, b, c))