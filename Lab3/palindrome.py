string1 = input("Enter a word: ")
string2 = string1[::-1]
if (string2 == string1):
  print("This word is a palindrome")
else:
  print("This word is not a palindrome")