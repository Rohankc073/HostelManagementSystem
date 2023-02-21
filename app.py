# print('p\"yth"on') #to give quotation
# print("Hello \n Python") #to write my code in the next line
# print("Helloo\b Python")   #to delete one letter
# print("Helloo\b\b Python")  # to delete two letters we need add one more backslash b and more depending on our preference
# print("Hello \\ Python")# to add backslash in in my code and increase it by two like 2*2
# print("Hello Python")
# print(" \t python") # to leave a defult space like 6 space in Pycharm and 8 in VS Code
# print("\t Pyhton".expandtabs(tabsize=6))#to leave space before the word but to our own preference
# print(r"Hello\npython")#by adding r before our code the string remains unchanged even if we add any escape sequence
# a="Python"
# b=a.replace('P',' ')#if you want to replace any word instead of P instead of leaving a space between the qoutation just add any word
# print(b)
# a='pyhton'#to skip values in index number
# print(a[0:5:3])
# a="Python"#to add any values in a string
# b='t'+a
# print(b)
# a="Python"
# b=a[ :3]+'m'+a[3: ]# to add any letter in the middle of the string
# print(b)
# a="Ppython"
# b=a[ :1]+'m'+a[2: ]#to remove as wellas to add any letter in the string the same time
# print(b)
# a="Python Hello"
# print(len(a))#to find the length of the string
# a='Python Hello'
# b=a.replace(" ",'')
# print(b)
# a="    Python Hello" #it removes the blank space which are the left side of the string
# b=a.lstrip()
# print(b)
# a="python hello    "#it removes the blank space which are the right sdie of the string
# b=a.rstrip()
# print(b)
# a="  Python Hello   "#it removes the blank space from both side of the string
# b=a.strip()
# print(b)
# a="python hello "
# b=a.title()#it turns all the first letter of a string into capital letter
# print(b)
# a="python hello"#it turn all the letters in the string into capital or vise versa
# b=a.swapcase()
# print(b)
# a="python hello"#it turns all the letters into capital letter
# b=a.upper()
# print(b)
# a="PYTHON HELLO"#it turns all the letter in the string into lower case
# b=a.lower()
# print(b)
# a="python hello"#it turns the first letter of the string into capital letter
# b=a.capitalize()
# print(b)
# a="python"
# b=a.isupper()#this is a boolean value which shows if the string is in an upper case or not, if the string is not in uppercase it returns false and vice versa
# print(b)
# a="Python"
# b=a.islower()#it tells us weather the string is in upper or lower case, even if one letter is in upper then the result is false which means all the letters must be in lower case for it to come true
# print(b)
# a="Python Hello "
# b=a.istitle()#it shows weather the first letter of an string is in capital or small letter, if it is in small the ans if false and vice versa, but even if one word has small letter in its beginning the answer is false which means all the beginning words in a string musdt be capital letter for it to come true
# print(b)
# #.isdigit, this tells us weather the string is a digit or an alphabet, even if one value of the string is an alphabet the answer will be false
# a="Python1"
# b=a.isdigit()
# print(b)
# #.is aplha, this shows weather all the values in a  string an alphabet or not
# a="Python1"
# b=a.isalpha()
# print(b)
# #.isalum, this shows us weather thee values in a string is an alphabet or a digit,even if the values are digit or alphabet or the mixture of both the ans is true
# a="py123"
# b=a.isalnum()
# print(b)
# #.isprintable, this show us weather the values in the string is printable or not, like if we add any escape sequence in the string it is not printable which means the sequences are not directly printed and so the answer is false
# a="Python\nhello"
# b=a.isprintable()
# print(b)
# #.isspace, this shows us weather there is a blank space in the string or not, if the yes then it is true but even if there is a single letter then the value is false which means the entire string must be completely empty
# a="Pyt hon"
# b=a.isspace()
# print(b)
# a="\t"#this is ,isspace and the ans is true because the escape sequence is not printable and hence the string is actually empty
# b=a.isspace()
# print(b)
# #.isidentifier,this shows us weather the string is uding the law of identifer, means like twe cannot use numbers on the start of the string and so on
# a="1ython"
# b=a.isidentifier()
# print(b)
# a="Python111"#it shows how many times a particular letter or word has been used in a string
# b=a.count('1')
# print(b)
# a="hello python"
# b=a.index('p')#this helps us find the index of a particluar letter on a stirng from left to right
# print(b)
# a="hello world"
# b=a.rindex('o')#even this helps us find the index of a letter but from right to left
# print(b)
# a="pypn"
# b=a.find('m')#even this helps to find the index of a letter in the string from left to right but if the letter is not in the string the ans will be -1 a
# print(b)
# a="Pypnoo"
# b=a.rfind('o')#this is same as find but this finds the index number from right to left and the answer is never negative if the ans is negative then the letter is not in the string
# print(b)
# a="Python Hello"
# b=a.center(16)#this function will leave the space in the front and the back and makes keeps the string in the middle like as i have written 16 and the string has only 11 index it keeps the string in the middle and makes the string of 16 index
# print(b)
# a="Hello python"
# b=a.center(16,'*')#this function is the same as center but i have just added * instead of the black space left in the previous one which means the blank space is replaced by the * sign
# print(b)
# a="Hello Python"
# b=a.zfill(16)#this is quite the same as the center function but in this the instead of the blank space 0 is added and only in the front and not at the back
# print(b)

