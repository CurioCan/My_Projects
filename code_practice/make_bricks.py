def make_bricks(small, big, goal):
  if goal > big * 5 + small:
    return False
  elif goal % 5 > small:
    return False
  else:
    return True
# 3, 1, 8 -> True
# 3, 1, 9 -> False
# Think of the cases when it fails

# evenif add total number of bricks we had doesn't make goal
# not enough small bricks

# so think of the cases when it fails