a, b = map(int, input().split())

list_signal = input().split()

check = True

if len(list_signal) <= 2:
    print("-1")

elif len(list_signal) == 3:

    test_min = int(list_signal[1])

    test_max_left = int(list_signal[0])

    test_max_right = int(list_signal[2])

    if (test_max_left - test_min) >= b and (test_max_right - test_min) >= b:
        print(test_max_right + test_max_left - 2 * test_min)
        check = False
else:

    for i in range(1, (len(list_signal) - 1)):

        test_min = int(list_signal[i])

        left_list = list_signal[0:i]
        test_max_left = int(max(left_list))

        if i != len(list_signal) - 2:
            right_list = list_signal[(i + 1):-1]
            test_max_right = int(max(right_list))
        else:
            test_max_right = int(list_signal[-1])

        if (test_max_left - test_min) >= b and (test_max_right - test_min) >= b:
            print(test_max_right + test_max_left - 2 * test_min)
            check = False
            break

if check:
    print("-1")
