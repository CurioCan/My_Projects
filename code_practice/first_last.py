def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]


# squirrel party
def cigar_party(cigars, is_weekend):
    if is_weekend:
        return (cigars >= 40)
    else:
        return (cigars >= 40 and cigars <= 60)

# stylish if the value is greater than 8
def date_fashion(you, date):
    if you <= 2 or date == 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    return 1

# police caught
def caught_speeding(speed, is_birthday):
    extra = 5 if is_birthday else 0
    if speed <= 60 + extra:
        return 0
    elif speed <= 80 + extra:
        return 1
    else:
        return 2

# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.
def near_ten(num):
  if (num % 10) <= 2 or (num % 10) >= 8:
    return True
  return False
