def count_left(n, k):
    left = 1
    if n > k - n:
        n = k - n
    for i in range(0, n):
        left *= (k - i)
        left /= (i + 1)

    return left


def solve(n, k):
    count = 0
    if n < k:
        return 0
    count = count_left(k - 1, k + n - 1)
    return int(count)


a, b = map(int, input().split())

result = solve(a, b)
print(result % (10 ** 9 + 7))
