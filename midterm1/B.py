string = input()
count = 0
for x in range(len(string)):
    for y in range(x, len(string)):
        # print(string[x:y+1], end=" ")

        # yolo = string[x:y+1]

        if string[x:y+1] == string[x:y+1][::-1]:
            # print("YO")
            count += 1
        # else:
        #     print("")

# print("")
print(count)
