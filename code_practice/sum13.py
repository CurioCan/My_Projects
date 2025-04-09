# Return sum
# except the number 13 is very unlucky, so it does not count
# and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 13, 2, 1, 13]) -> 4
def sum13(nums):
    sum = 0
    if len(nums) == 0:
        return 0
    else:
        for i in range(len(nums)):
            if i == 0:
                sum += 0 if nums[0] == 13 else nums[0]
            else:
                if nums[i] == 13 or (nums[i - 1] == 13 and i > 0):
                    sum += 0
                else:
                    sum += nums[i]
    return sum

# making it more shorter
def sum13(nums):
    if not nums:
        return 0
    total = 0
    for i in range(len(nums)):
        if nums[i] == 13 or (i > 0 and nums[i-1] == 13):
            continue
        total += nums[i]
    return total