from copy import deepcopy as dp

lame = input()
data = list(map(int, input().split()))
sub = []

x = 0
y = 0

x_a = []
y_a = []
y_tmp_a = []

for i in range(len(data)):
    y_tmp = max(x, y)
    if y > x:
        y_tmp_a = y_a
        x_a.clear()
    else:
        y_tmp_a = x_a
        y_a.clear()

    x = y + data[i]
    x_a.append(i)

    y = y_tmp
    y_a = y_tmp_a

    if x > y:
        sub.append(i + 1)

# print(x_a)
# print(y_a)
#
#
# print(max(x, y))
# print(len(sub))
# for ele in sub:
#     print(ele, end=" ")

new_sub = []
for i in range(len(sub) - 1):
    if (sub[i] + 1) == sub[i + 1]:
        sub[i] = None

for i in range(len(sub)):
    if sub[i] is not None:
        new_sub.append(sub[i])

print(len(new_sub))
for ele in new_sub:
    print(ele, end=" ")
