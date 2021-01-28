from itertools import permutations


num = int(input())

list_num = [str(i) for i in range(1, num+1)]

permutation_list = tuple(permutations(list_num))

for perm in list(permutation_list):
    print(' '.join(perm))

