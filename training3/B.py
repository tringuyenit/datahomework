# n, b = map(int, input().split())
different_weight = []
#
# data = [tuple(input().split()) for i in range(n)]


n = 24
b = 6404180

x = [input() for i in range(n)]
y = [input() for i in range(n)]

data = []

for i in range(n):
    new_set = [x[i], y[i]]
    data.append(new_set)


for item in data:
    if item[0] not in different_weight:
        different_weight.append(item[0])

different_weight.sort()

# print(data)
# print(different_weight)

number_different_weight = len(different_weight)

weight_classified = []

for i in range(number_different_weight):

    new_weight = []

    for w in data:
        if different_weight[i] == w[0]:
            new_weight.append(w)

    new_weight.sort(key=lambda ele: ele[1])
    weight_classified.append(new_weight)


def print_class_weight(weight):
    print("=========================")
    print(" ( w ,  q)")
    for row in weight:
        print(row)
    print("=========================")


# print_class_weight(weight_classified)

count_remove = 0
for row in weight_classified:
    if int(row[0][0]) > b:
        count_remove += 1

for i in range(count_remove):
    weight_classified.pop(-1)

# print_class_weight(weight_classified)

consumed_weight = 0
quality = 0

able_to_choose = True
while consumed_weight < b and len(weight_classified) != 0 and able_to_choose:

    best_choice = None  # index
    best_w_per_unit = 0

    for row in weight_classified:
        if b-consumed_weight < int(row[0][0]):
            print(0, int(row[-1][1])/int(row[-1][0]))
            continue

        if int(row[-1][1]) == 0:
            print(0, int(row[-1][1])/int(row[-1][0]))
            continue

        if int(row[-1][0]) == 0:
            w_per_unit = (int(row[-1][1])+100) ** 2  # for fun :)))
        else:
            w_per_unit = int(row[-1][1]) / int(row[-1][0])

        if w_per_unit > best_w_per_unit:
            best_w_per_unit = w_per_unit
            best_choice = weight_classified.index(row)

    if best_choice is not None:
        a = int(weight_classified[best_choice][-1][1])
        b = int(weight_classified[best_choice][-1][0])
        print(1, (a/b))
        consumed_weight += int(weight_classified[best_choice][-1][0])
        quality += int(weight_classified[best_choice][-1][1])

        weight_classified[best_choice].pop(-1)
        if len(weight_classified[best_choice]) == 0:
            weight_classified.pop(best_choice)
    else:
        able_to_choose = False

# print(consumed_weight)
print(quality)

