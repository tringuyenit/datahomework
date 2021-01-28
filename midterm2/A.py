lame = input()

data = input().split()

# print(data)

if len(data) == 0:
    print(0)
    exit(0)

count = 0

for i in range(len(data)):
    if data[i] < data[i-1]:
        count += 1

print(count+1)