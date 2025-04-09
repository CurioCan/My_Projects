def sum67(nums):
    if not nums:
        return 0

    sum = 0
    skip = False

    for i in range(len(nums)):
        if nums[i] == 6:
            skip = True
        if not skip:
            sum += nums[i]
        elif nums[i] == 7:
            skip = False
    return sum


# problem statement return sum
# except ignore sections of num starting with 6 and extending
# to the next 7
# every 6 will be followed by atleast one 7
