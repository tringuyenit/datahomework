from copy import deepcopy as dp

trash = input()
data = input().split()

best = dp(data)
best.sort()
best.reverse()

# print(data)
# print(best)

if data == best:
    print("-1")
    exit(0)
else:
    need_change = data[-1]
    pos = len(data) - 2

    for i in range(len(data)-1):
        if data[len(data) - i - 2] >= need_change:
            pos -= 1
        else:
            data.insert(pos, need_change)
            data.pop(-1)
            break

# print(data)

for e in data:
    print(e, end=" ")
