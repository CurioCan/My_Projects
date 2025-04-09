# big_diff
def max(a, b):
    return a if a > b else b


def min(a, b):
    return a if a < b else b


def big_diff(nums):
    smallest = nums[0]
    largest = nums[0]
    if len(nums) == 1:
        return 0
    elif len(nums) == 2:
        return abs(nums[0] - nums[1])
    else:
        for i in range(len(nums)):
            if max(largest, nums[i]) != largest:
                largest = nums[i]
            if min(smallest, nums[i]) != smallest:
                smallest = nums[i]

    return abs(smallest - largest)



# builtin- functions
# python
# return max(nums) - min(nums)
# max() min() sum() len()

'''''
centered average don't include max and min 
of the array of ints and return int division
'''''
def centered(nums):
    nums.sort()
    return sum(nums[1:-1] // len(nums[1:-1]))
# return sum(nums[1:-1] // (len(nums)-2)
#sum