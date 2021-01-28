def permutaion(num):
    ans = 1
    for i in range(num):
        ans *= (i + 1)
    return ans


def combination(num, k):
    return int(permutaion(num) / (permutaion(k) * permutaion(num - k)))


def solve(n, k):
    if n == 0 or k == 0:
        print(-1)
    if n < 0 or k < 0 :
        print(-1)

    else:
        multi = 0
        check = False

        if n < k:
            multi = combination(k, n)
            k = n
            check = True

        solution = 0
        for i in range(k):
            solution += combination(k, k - i) * combination(n - 1, k - 1 - i)

        if check:
            solution *= multi

        print(solution % (10 ** 9 + 7))


a, b = map(int, input().split())

solve(a, b)
