# check whether xyz is there or not
# if it is preceeded by . then ignore doing so
def xyz_there(s):
    for i in range(len(s)):
        if s[i:i+3] == 'xyz' and (i == 0 or s[i-1]!= '.'):
            return True
    return False

# def xyz_there(str):
#   count = 0
#   for i in range(len(str) - 2):
#     if i == 0:
#       if str[:3] == 'xyz':
#         count += 1
#     else:
#       if str[i:i+3] == 'xyz' and str[i-1] == '.':
#         count += 0
#       elif str[i:i+3] == 'xyz':
#         count += 1
#   if count > 0:
#     return True
#   else:
#     return False