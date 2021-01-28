from math import pi as pi

test_num = int(input())

data = []
for i in range(test_num):
    new_data = list(map(int, input().split()))
    radii_squared = int(input()) ** 2
    new_data.append(radii_squared)
    data.append(tuple(new_data))

for da in data:

    if da[1] == 0:
        print("0")
    else:
        total_v = da[0] * da[2] * pi
        print(round(total_v / da[1], 6))
