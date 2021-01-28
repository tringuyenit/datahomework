from copy import deepcopy as dp
from numpy import transpose as trans

number_queen = 0
final_forms = []


# Transform
def rotate_board2(board):
    size = len(board)
    # Consider all squares one by one
    for x in range(0, int(size / 2)):
        # Consider elements in group
        # of 4 in current square
        for y in range(x, size - x - 1):
            # store current cell in temp variable
            temp = board[x][y]

            # move values from right to top
            board[x][y] = board[y][size - 1 - x]

            # move values from bottom to right
            board[y][size - 1 - x] = board[size - 1 - x][size - 1 - y]

            # move values from left to bottom
            board[size - 1 - x][size - 1 - y] = board[size - 1 - y][x]

            # assign temp to left
            board[size - 1 - y][x] = temp

        return board


def rotate_board(board):
    size = len(board)
    # tmp_board = dp(board)
    # Consider all squares one by one
    tmp_board = list(list(x)[::-1] for x in zip(*board))
    for row in range(size):
        for ele in range(size):
            board[row][ele] = tmp_board[row][ele]

    return tmp_board


def flip_board_vertical(board):
    tmp_board = dp(board)
    for row in tmp_board:
        for i in range((len(row) + 1) // 2):
            row[i], row[len(row) - 1 - i] = row[len(row) - 1 - i], row[i]

    return tmp_board


def flip_board_horizontal(board):
    tmp_board = dp(board)
    for i in range((len(tmp_board) + 1) // 2):
        tmp_board[i], tmp_board[len(tmp_board) - 1 - i] = tmp_board[len(tmp_board) - 1 - i], tmp_board[i]

    return tmp_board


def flip_diag_1(board):
    tmp_board = trans(board)
    return tmp_board


def flip_diag_2(board):
    tmp_board = trans(flip_board_vertical(flip_board_horizontal(board)))
    return tmp_board


def store_all_forms(board):
    all_forms = []

    tmp = dp(board)
    flip_ver = flip_board_vertical(board)
    flip_hor = flip_board_horizontal(board)
    flip_diag1 = flip_diag_1(board)
    flip_diag2 = flip_diag_2(board)

    for i in range(4):
        all_forms.append(rotate_board(tmp))

    for i in range(4):
        all_forms.append(rotate_board(flip_hor))

    for i in range(4):
        all_forms.append(rotate_board(flip_ver))

    for i in range(4):
        all_forms.append(rotate_board(flip_diag1))

    for i in range(4):
        all_forms.append(rotate_board(flip_diag2))

    # print(len(all_forms))
    # for i in range(20):
    #     print_board(all_forms[i])
    #     if i == 3 or i == 7 or i == 11 or i == 15:
    #         print("================")

    check_tmp = False
    for i in range(4):
        if all_forms[i] in final_forms:
            check_tmp = True
    if not check_tmp:
        tmp_fake = dp(all_forms[0])
        final_forms.append(tmp_fake)

    check_ver = False
    for i in range(4, 8):
        if all_forms[i] in final_forms:
            check_ver = True
    if not check_ver:
        tmp_flip_ver = dp(all_forms[4])
        final_forms.append(tmp_flip_ver)

    check_hor = False
    for i in range(8, 12):
        if all_forms[i] in final_forms:
            check_hor = True
    if not check_hor:
        tmp_flip_hor = dp(all_forms[8])
        final_forms.append(tmp_flip_hor)

    check_diag1 = False
    for i in range(12, 16):
        if all_forms[i] in final_forms:
            check_diag1 = True
    if not check_diag1:
        tmp_flip_diag1 = dp(all_forms[12])
        final_forms.append(tmp_flip_diag1)

    check_diag2 = False
    for i in range(16, 20):
        if all_forms[i] in final_forms:
            check_diag2 = True
    if not check_diag2:
        tmp_flip_diag2 = dp(all_forms[16])
        final_forms.append(tmp_flip_diag2)

    # for form in final_forms:
    #     print_board(form)


# Logic
def create_board(board_size):
    complete_board = [[" " for i in range(board_size)] for j in range(board_size)]
    return complete_board


def print_board(board):
    for row in range(len(board)):
        for ele in range(len(board[row])):
            if ele != len(board) - 1:
                print(board[row][ele], end="  ")
            else:
                print(board[row][ele])

    print("")


def find_empty_spot(board):
    for row in range(len(board)):
        for ele in range(len(board[row])):
            if board[row][ele] != "#" and board[row][ele] != "Q" and board[row][ele] != "&":
                return row, ele

    return None


def control_squares(spot, board):
    # spot is tuple from find_empty_spot()

    number_controlled = 0
    spot_controlled = []

    # Place the Queen
    board[spot[0]][spot[1]] = "Q"
    spot_controlled.append((spot[0], spot[1]))
    global number_queen
    number_queen += 1

    # Control row aka spot[0]
    for ele in range(len(board[spot[0]])):
        if ele != spot[1]:  # not current spot (row)
            if board[spot[0]][ele] != "#":
                board[spot[0]][ele] = "#"
                number_controlled += 1
                spot_controlled.append((spot[0], ele))

    # Control column aka spot[1]
    for column in range(0, len(board)):
        if column != spot[0]:  # not current spot (column)
            if board[column][spot[1]] != "#":
                board[column][spot[1]] = "#"
                number_controlled += 1
                spot_controlled.append((column, spot[1]))

    # Control diagnol
    for row in range(0, len(board)):
        if row != spot[0]:
            tmp1 = spot[1] - spot[0] + row
            tmp2 = spot[0] + spot[1] - row

            if 0 <= tmp1 <= len(board) - 1:
                if board[row][tmp1] != "#":
                    board[row][tmp1] = "#"
                    number_controlled += 1
                    spot_controlled.append((row, tmp1))

            if 0 <= tmp2 <= len(board) - 1:
                if board[row][tmp2] != "#":
                    board[row][tmp2] = "#"
                    number_controlled += 1
                    spot_controlled.append((row, tmp2))

    return [number_controlled, spot_controlled]


def undo_control(spots, board):
    # spots is list of controlled spots from control_squares()

    global number_queen
    number_queen -= 1

    for spot in spots:
        board[spot[0]][spot[1]] = " "


def lock_wrong_spot(number, board):
    done = 0
    size = len(board)

    if number == 0:
        return None

    for row in range(size):
        for ele in range(size):
            if board[row][ele] == " ":
                board[row][ele] = "&"
                done += 1

                if done == number:
                    return None


def unlock_wrong_spot(number, board):
    done = 0
    size = len(board)

    if number == 0:
        return None

    for row in range(size):
        for ele in range(size):
            if board[size - row - 1][size - ele - 1] == "&":
                board[size - row - 1][size - ele - 1] = " "
                done += 1

                if done == number:
                    return None


def check_full_now(board):
    size = len(board)

    for row in range(size):
        for ele in range(size):
            if board[row][ele] == " ":
                return False

    return True


def backtracking(board):
    # # SHOW STEPS
    # print("")
    # print_board(board)

    global number_queen

    empty_spot = find_empty_spot(board)

    if number_queen == len(board) and empty_spot is None:
        number_queen = 0
        return True

    tmp = control_squares(empty_spot, board)
    # print_board(board)
    num_wrong_spot = 0

    while True:
        lock_wrong_spot(num_wrong_spot, board)

        if check_full_now(board) and number_queen != len(board):
            unlock_wrong_spot(num_wrong_spot, board)
            undo_control(tmp[1], board)
            break

        # if check_full_now(board) and number_queen == 8:
        #     unlock_wrong_spot(num_wrong_spot, board)
        #     undo_control(tmp[1], board)
        #     break

        if not backtracking(board):
            unlock_wrong_spot(num_wrong_spot, board)
            num_wrong_spot += 1
        else:
            return True

    return False


def trial(num, board_size):
    board = create_board(board_size)
    lock_wrong_spot(num, board)

    if backtracking(board):
        print("[", num + 1, "]")
        print_board(board)
        store_all_forms(board)
        return True  # do not remove this line !!!


def solve():
    board_size = int(input("Board size ? : "))

    have_solution = False

    for x_pos in range(board_size):
        if trial(x_pos, board_size):
            have_solution = True

    if not have_solution:
        print("No solution :(")
    else:

        print("=================")
        print("      FINAL      ")
        for form in final_forms:
            print_board(form)
        print(len(final_forms))
        print("HERRE")


# RUN
solve()
