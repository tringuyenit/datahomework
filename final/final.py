num_case = int(input())
data = []
t = []
money = []

for i in range(num_case):
    data.append([])

for i in range(num_case):
    a, b = map(int, input().split())
    t.append(b)
    for x in range(a):
        m, n = map(int, input().split())
        data[i].append((n, m))
print(data)

a = None
b = []
for i in range(num_case):
    num = []
    for tup in data[i]:
        num.append(tup[0])
    x = list(set(num))
    x.sort()
    y = len(x)
    print(y)

    a = sorted(data[i], key=lambda dm: (dm[0], not dm[1]))

    print(a)
    sub_data = []

    print(sub_data)
    print(x)

    print()
    start = 0
    p = 0
    for number in x:
        sub_sub = []
        while p < len(a):

            if number == a[p][0]:
                sub_sub.append(a[p])
            else:
                sub_data.append(sub_sub)
                break
            p += 1
            if p == len(a):
                sub_data.append(sub_sub)
                break
    print(sub_data)
    b.append(sub_data)
print("b = ", b)


for i in range(num_case):
    if len(b[i]) == 0:
        money += 0
        break
    if len(b[i]) == 1:
        if b[i][0][0] == 0:
            tmp = 0
            for m in b[i]:
                tmp += b[i][0][1]
            money += tmp
        else:
            x = t[i] // b[i][0][0]
            tmp = 0
            for m in range(x):
                tmp += b[i][m][1]
            money += tmp
    else:
        p1 = 0
        p2 = 1
        while p1 < len(b[i]) - 1:
            p

print(money)



