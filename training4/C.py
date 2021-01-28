trash, need = map(int, input().split())

data = list(map(int, input().split()))
data.sort()
data.reverse()

length = data[0]

p1 = int(length / 2)
p2 = 1
p3 = length


def check_more():
    cur_height = length - p1
    all_height = 0

    for da in data:
        if da <= cur_height:
            break
        else:
            all_height += da - cur_height

    if all_height > need:
        return True
    elif all_height < need:
        return False
    else:
        return None


# count = 0

while True:
    # print("G", p2, p1, p3)

    check = check_more()

    if check is True:
        new_p1 = int((p1 - p2) / 2)

        if new_p1 == p1:
            break
        else:
            p3, p1 = p1, new_p1

    elif check is False:
        new_p1 = p1 + int((p3 - p1) / 2)

        if new_p1 == p3:
            break
        else:
            p2, p1 = p1, new_p1

    else:
        break

print(length - p1)
