# def array_front9(nums):
#   count = 0
#   if len(nums) < 4:
#     if len(nums) == 0:
#       count = 0
#     else:
#       for i in range(len(nums)):
#         if nums[i] == 9:
#           count += 1
#   else:
#     for i in range(4):
#       if nums[i] == 9:
#         count += 1
#   if count > 0:
#     return True
#   else:
#     return False
#
'''
shorter version of this
'''
def array_front9(nums):
    return any(num == 9 for num in nums)
# problem statement
# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
#
array_front9([1, 2, 9, 3, 4])
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False