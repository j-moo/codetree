def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


def solve(idx, result):
    if idx == n:
        return result

    return solve(idx + 1, lcm(result, arr[idx]))


n = int(input())
arr = list(map(int, input().split()))

print(solve(1, arr[0]))