nah = int(input())

datas = []

for i in range(nah):
    datas.append(input())


def check(inp, wait):
    if inp == ')':
        if wait == '(':
            return True
        else:
            return False

    if inp == ']':
        if wait == '[':
            return True
        else:
            return False

    if inp == '}':
        if wait == '{':
            return True
        else:
            return False


for data in datas:

    stack_wait = [data[0]]
    wait_index = 0

    for i in range(1, len(data)):

        if len(stack_wait) != 0:

            if check(data[i], stack_wait[-1]):
                stack_wait.pop(wait_index)
                wait_index -= 1
            else:
                stack_wait.append(data[i])
                wait_index += 1

        else:
            stack_wait.append(data[i])
            wait_index += 1

    if len(stack_wait) == 0:
        print("1")
    else:
        print("0")
