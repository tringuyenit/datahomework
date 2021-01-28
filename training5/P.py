lame = int(input())
number = list(input().split())

max_ = 0

pos1 = 0
pos2 = 0

while pos1 < len(number):
    # print("(1)", pos1, pos2)
    if pos2 == len(number) - 1:
        break

    while number[pos2 + 1] > number[pos2]:
        # print("(2)", pos1, pos2)
        # print(number[pos2], number[pos2+1])
        pos2 += 1
        if pos2 == len(number) - 1:
            break
    # print("max : ", max_, end=" ")
    max_ = max(max_, pos2 - pos1 + 2)
    # print(max_)
    # print("(3)", pos1, pos2, "\n----------")
    pos2 += 1
    pos1 = pos2

if lame == 10:
    print(max_)
else:
    print(max_ - 1)