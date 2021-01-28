node_list = [[0, 0]]  # init with 0 position

distance = 0
position_of_0_in_list = 0

a, b = map(int, input().split())

for i in range(a):
    node_location, node_num = map(int, input().split())
    this_node = [node_location, node_num]
    node_list.append(this_node)

    if node_location < 0:
        position_of_0_in_list += 1

node_list.sort(key=lambda e: e[0])

position = 0

position -= 0
direction = 2  # 1 is left, 2 is right
distance = abs(node_list[position][0])
remaining = b

# print("pos :", position, end=" ")
# print("|dis :", distance, end=" ")
# print("|remain :", remaining)
# # print("|dir :", direction)
# print(node_list, end="\n\n")

c = 0
tmp = 0

while a != 0:

    # print("pos :", position, end=" ")
    # print("|dis :", distance, end=" ")
    # print("|remain :", remaining)
    # print(node_list, end="\n")

    if remaining == 0:
        distance += 2 * abs(node_list[position][0])  # get back
        remaining = b  # refill
    else:
        if node_list[position][0] != 0:
            a -= 1

        if remaining >= node_list[position][1]:
            remaining -= node_list[position][1]
            node_list[position][1] = 0

            if position + 1 < len(node_list):
                distance += abs(abs(node_list[position][0]) - abs(node_list[position + 1][0]))

            position += 1
        else:
            if (node_list[position][1] - remaining) > b:

                last = (node_list[position][1] - remaining) % b
                times_to_return = (node_list[position][1] - remaining) // b

                if last > 0:

                    # node_list[position][1] -= remaining

                    distance += times_to_return * 2 * abs(node_list[position][0])
                    # node_list[position][1] -= times_to_return * b

                    distance += times_to_return * 2 * abs(node_list[position][0])
                    # node_list[position][1] -= last
                    node_list[position][1] = 0
                    remaining = b - last

                    position += 1
                else:

                    # node_list[position][1] -= remaining

                    distance += times_to_return * 2 * abs(node_list[position][0])
                    # node_list[position][1] -= times_to_return * b
                    node_list[position][1] = 0

                    if position + 1 < len(node_list):
                        distance += (abs(node_list[position][0]) + abs(node_list[position + 1][0]))
                    remaining = b

                    position += 1

            else:
                node_list[position][1] -= remaining

                times_to_return = 1
                distance += times_to_return * 2 * abs(node_list[position][0])

                remaining = b - node_list[position][1]
                node_list[position][1] = 0

                distance += abs(abs(node_list[position][0]) - abs(node_list[position + 1][0]))

                position += 1

    # print("pos :", position, end=" ")
    # print("|dis :", distance, end=" ")
    # print("|remain :", remaining, "a=", a, end="\n\n\n")

distance += abs(node_list[position - 1][0])
# print(node_list)
print(distance)
