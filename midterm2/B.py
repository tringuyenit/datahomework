lame = input()

data = list(map(int, input().split()))
data.reverse()

string = list(map(str,input()))

gate = []

# print(data)

for i in range(len(string)):
    if string[i] == 'C':
        gate.append(data.pop(-1))

    else:
        data.append(gate.pop(0))

data.reverse()

for i in data:
    print(i, end=" ")



