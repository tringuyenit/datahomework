l = [500, 100, 50, 10, 5, 1]
num_note = 0

val = int(input())
back = 1000 - val

start = 0

while l[start] > back:
    start += 1

tmp = int(back / l[start])

while back != 0:

    int(back / l[start])
    print("tmp ", tmp)
    num_note += tmp
    back -= l[start] * tmp
    print("back ", back)
    print("val ", l[start])
    print("num ", num_note, end="\n\n")

    if start == 5 and back == 0:
        break

    if l[start] > back:
        start += 1

print("\n@@@@\na ", tmp)
print("b ", back)
print("c", num_note)

print(num_note + back)
