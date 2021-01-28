def maxSubArray(nums):
    tmp = [nums[0]]

    for i in range(1, len(nums)):
        tmp.append(max(tmp[i - 1] + nums[i], nums[i]))
    return max(tmp)


list_len = int(input())

numbers = [-2, 1, -3, 7, -2, 2, 1, -5, 4]
print(maxSubArray(list(map(int, input().split()))))
