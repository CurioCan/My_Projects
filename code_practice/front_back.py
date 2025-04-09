def front_back(str):
  if len(str) == 0:
    return ""
  elif len(str) == 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]

check = front_back("Chocolate")
print(f"Chocolate is modified to \"{check}\"")