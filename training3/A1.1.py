from itertools import permutations

n, m = map(int, input().split())

data = {}
path = []

for i in range(m):
    new_data = tuple(input().split())
    data[(new_data[0], new_data[1])] = new_data[2]


# print(data)

def pre_process_data(datas):
    actual_nodes = [str(x + 1) for x in range(n)]
    different_nodes = []
    for tup in datas:
        if tup[0] not in different_nodes:
            different_nodes.append(tup[0])
        if tup[1] not in different_nodes:
            different_nodes.append(tup[1])

    different_nodes.sort()
    # print(different_nodes)
    # print(actual_nodes)

    real_dict = dict(zip(different_nodes, actual_nodes))
    # print(real_dict)

    new_datas = {}
    for tup in datas:
        actual_1 = real_dict[tup[0]]
        actual_2 = real_dict[tup[1]]
        the_cost = datas[tup]

        new_datas[(actual_1, actual_2)] = the_cost

    return new_datas


# print(data)
data = pre_process_data(data)
# print(data)

node = []

for i in range(n - 1):
    node.append(str(i + 2))

permutation_list = tuple(permutations(node))

# print(permutation_list)

if len(permutation_list) <= 1:
    print(sum(list(map(int, data.values()))))
else:
    for perm in permutation_list:
        trial = ["1"]
        cost = 0

        for start in range(n - 1):

            travel2 = None

            if start == 0:
                travel1 = ("1", perm[start])
            elif start == n - 2:
                travel1 = (perm[start - 1], perm[start])
                travel2 = (perm[start], "1")
            else:
                travel1 = (perm[start - 1], perm[start])

            if travel1 in data:
                if travel2 is not None:
                    if travel2 in data:
                        trial.append(perm[start])
                        trial.append("1")
                        cost += int(data[travel1]) + int(data[travel2])
                    else:
                        break
                else:
                    trial.append(perm[start])
                    cost += int(data[travel1])
            else:
                break
        if len(trial) == n + 1:
            trial.append(cost)
            path.append(trial)

    if len(path) != 0:
        path.sort(key=lambda x: x[-1])
        print(path[0][-1])
    # print(path)
