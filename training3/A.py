n, m = map(int, input().split())

data = [[] for i in range(n - 1)]
end_at_1 = []
start_from_1 = []
path = []
cost = 0
minimum_cost = []

for i in range(m):
    new_data = tuple(input().split())
    if new_data[1] == "1":
        end_at_1.append(new_data)
    elif new_data[0] == "1":
        start_from_1.append(new_data)
    else:
        data[int(new_data[1]) - 2].append(new_data)


def solve(datas, back):
    # print(path)
    if str(back) not in path:
        path.append(str(back))

        if len(data[back - 2]) == 0:
            for ele in start_from_1:
                if ele[1] == path[-1]:
                    path.append("1")
                    return True

            path.pop(-1)
            return False

        index = 0
        while index < len(data[back - 2]):
            next_back = int(data[back - 2][index][0])

            if solve(datas, next_back):
                return True
            else:
                index += 1

        path.pop(-1)
        return False

    else:
        for ele in start_from_1:
            if ele[1] == path[-1]:
                path.append("1")
                return True

        path.pop(-1)
        return False


# For testing :
# print(data)
# print(end_at_1)
# print(start_from_1)
# print("")

for test in end_at_1:
    path.append("1")
    if not solve(data, int(test[0])):
        path.pop(-1)

    # Reversed path :
    # print(path)

    # Real path :
    # path.reverse()
    # print(path)
    # path.reverse()
    # print("")

    if len(path) == n + 1:
        for e in range(1, n + 1):
            if e == n:
                # print("HERE 1")
                for start in start_from_1:
                    if path[e - 1] == start[1]:
                        # print(start[2])
                        cost += int(start[2])
                        break

            elif e == 1:
                # print("HERE 2")
                for end in end_at_1:
                    if path[e] == end[0]:
                        # print(end[2])
                        cost += int(end[2])
                        break

            else:

                # print("HERE 3")
                for nextt in data:
                    if path[e - 1] == nextt[0][1]:
                        for x in nextt:
                            if x[0] == path[e]:
                                # print(x[2])
                                cost += int(x[2])
                                break
    else:
        pass
        # print("CHUA DI QUA HET :(")

    # Final tmp cost :
    # print("")
    # print(cost)
    # print("")

    minimum_cost.append(cost)
    path.clear()
    cost = 0

# print(minimum_cost)
print(min(minimum_cost))
