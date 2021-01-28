n, m = map(int, input().split())
# print(n)
# print(m)

s = 0
for i in range(n+1):
    s += (2 * i + 1) ** 2

print(s % m)
