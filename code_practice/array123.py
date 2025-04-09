# check 123 sequence
# def array123(nums):
#   count = 0
#   if len(nums) < 3:
#     count = 0
#   elif len(nums) == 3:
#     if nums[0] == 1 and nums[1] == 2 and nums[2] == 3:
#       count = 1
#   else:
#     for i in range(len(nums) - 2):
#       if nums[i] == 1:
#         if nums[i+1] == 2:
#           if nums[i+2] == 3:
#             count += 1
#   if count > 0:
#     return True
#   else:
#     return False

# shorter form of the co
def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i:i+3] == [1, 2, 3]:
            return True
    return False