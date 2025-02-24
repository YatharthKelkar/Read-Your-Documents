#import os
#os.remove("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document (2).txt")
def opening():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    print(data)
    f.close()
def charecters():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    c = len(data)
    print(c)
    f.close()
def words():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    s = data.split()
    print(len(s))
    f.close()
def lowercase():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    lower = 0
    for x in data:
     if x.islower():
      lower = lower +1
    print("The number of lower case letters in the file is", lower)
    f.close()
def uppercase():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    upper = 0
    for x in data:
     if x.isupper():
      upper = upper +1
    print("The number of upper case letters in the file is", upper)
    f.close()
def digit1():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    digit = 0
    for x in data:
     if x.isdigit():
      digit = digit +1
    print("The number of digits in the file is", digit)
    f.close()
def line():
   f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
   data = f.readlines()
   print(len(data))
def wordsearch():
   f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
   data= f.read()
   word = input(" Enter a word to search. ")
   count1 = 0   
   s = data.split()
   for w in s:
      if w.lower() == word.lower():
         count1 = count1 + 1
   print("The number of times the word was spotted in this document is" , count1)
def charecter():
    f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
    data = f.read()
    z = input("Please input the charecter which you want to chek")
    charecters = 0
    for x in data:
     if x.lower() == z:
      charecters = charecters +1
    print("The number of letters in the file is", charecters)
    f.close()
def linestart():
   f = open("C:/Users/kelka/OneDrive/Documents/Coding/Projects/New folder/New Text Document.txt", "r")
   data = f.readlines()
   count = 0 
   for x in data:
      if x[0].lower() == "s":
         count = count + 1
   print("The number of lines starting with s is ", count)
linestart()