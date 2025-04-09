# Given a non-empty string like "Code" return a string like "CCoCodCode"
def string_splosion(str):
  if len(str) == 1:
    return str
  else:
    splosion = ""
    for i in range(len(str)):
      splosion += str[:i+1]
    return splosion
# abc : a(ab)(abc) so output : aababc