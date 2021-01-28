input()  # no need
list_num = list(map(int, input().split()))

print(sum(list_num) % (10 ** 9 + 7))
