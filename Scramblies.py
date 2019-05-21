from collections import Counter
def scramble(s1, s2):
  s1 = Counter(s1)
  s2 = Counter(s2)
  return all(s2[i] <= s1[i] for i in s2)
print(scramble('katas', 'steak'))


