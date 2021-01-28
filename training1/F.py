num_line = int(input())
line_list = [input() for i in range(0, num_line)]

for i in range(0, num_line):

    length = len(line_list[i]) - 2

    if length > 8:
        print(line_list[i][0], end='')
        print(length, end='')
        print(line_list[i][length + 1], end='')
    else:
        print(line_list[i])
