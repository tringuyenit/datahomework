max_length = int(input())
if max_length == 0:
    exit(0)

stop_point = "1" * max_length

i = 0

while True:

    i_binary = bin(i)[2:]

    num_for_zero = max_length - len(i_binary)

    for x in range(num_for_zero):
        print("0", end="")
    print(i_binary)

    if i_binary == stop_point:
        break

    i += 1
