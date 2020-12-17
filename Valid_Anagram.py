
def Valid_Anagram(s, t):
  s = sorted(s)
  t = sorted(t)

  if s == t:
    return True
  return False