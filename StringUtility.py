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
    if len(self.string)<=1:
      return self.string
    else:
      asteric= "*"
      returining_string=""
      first_letter= self.string[0]
      for i in range(len(self.string)):
        if i ==0:
          returining_string+= first_letter
        else:
          if self.string[i]== first_letter:
            returining_string+= asteric
          else:
            returining_string+= self.string[i]
    return returining_string
  def asciiSum(self):
    sum_of_ascii=0
    for i in range(len(self.string)):
      sum_of_ascii+= ord(self.string[i])
    return sum_of_ascii
  def cipher(self):
    encoded_string=""
    first_letter_lower="a"
    first_letter_upper="A"
    number_of_letter_in_alpha= 26
    wrap_around_increment= 1
    length_of_string=len(self.string)
    for i in range(len(self.string)):
      if self.string[i].isalpha():
        if self.string[i].isupper():
          wrapping_number= (ord(self.string[i])+length_of_string-ord(first_letter_upper))% number_of_letter_in_alpha
          encoded_string+= chr(ord(first_letter_upper)+wrapping_number)
        elif self.string[i].islower():
          wrapping_number= (ord(self.string[i])+length_of_string-ord(first_letter_lower))% number_of_letter_in_alpha
          encoded_string+= chr(ord(first_letter_lower)+wrapping_number)
      else:
        encoded_string+= self.string[i]
    return encoded_string