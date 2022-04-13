class StringUtility:
  def __init__(self, string):
    self.string= string

  def __str__(self):
    #new_string= ""
    #new_string += self.string
    return self.string
  def vowels(self):
    count=0
    vowels= ("a","e","i","o","u")
    for i in range(len(self.string)):
      for vowel in vowels:
        if vowel == self.string[i]:
          count +=1
    if count>=5:
      count="many"
      return count
    else:
      return str(count)
  def bothEnds(self):
    bothends= ""
    if len(self.string) <=2:
      return bothends
    else:
      for i in range(2):
        bothends+= self.string[i]
      for j in range(-2,0):
        bothends+= self.string[j]
      return bothends
  def fixStart(self):
    
  #def asciiSum(self):
  #def cipher(self):


