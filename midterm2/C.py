# from copy import deepcopy as dp
#
# # lame = input()
#
# data = list(map(int, input().split()))
# # print(data)
#
# case = 0
#
# for i in data:
#     if i >= 0:
#         case = 1
#         break
#
# if case == 1:
#
#     check_none = False
#     for i in range(len(data)):
#         if data[i] < 0:
#             check_none = True
#             data[i] = None
#
#     all_group = []
#     tmp = []
#     for x in data:
#         if x is not None:
#             tmp.append(x)
#         else:
#             tmp2 = dp(tmp)
#             all_group.append(tmp2)
#             tmp2.clear()
#             tmp.clear()
#
#     s = 0
#     for g in all_group:
#         s += max(g)
#
#     print(s)
#
#
#
# else:
#     print(max(data))
