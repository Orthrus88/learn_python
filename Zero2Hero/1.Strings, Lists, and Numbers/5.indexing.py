'''
indexing
h e l l o
0 1 2 3 4

reverse indexing
h  e  l  l  o
0 -4 -3 -2 -1

slicing - sub secion of string
[start:stop:step]
'''

#INDEXING AND SLICING WITH STRINGS

mystr = 'hello world'
# indexing
'''
print(mystr[0]) # print first letter of mystr
print(mystr[-1]) # print last letter of mystr
print(mystr[5]) # print 6th leter of mystr
'''
# slicing
'''
mystr = 'abcdefghijk'
print(mystr[2:]) # print everything from index 2 to the end
print(mystr[:3]) # print everything from index 0 to 2. 3 denotes up to but does not include
print(mystr[3:6]) # print index 3 - 5
print(mystr[1:3]) # print index 1 and 2
print(mystr[::]) # print from begining to end 'but why?'
print(mystr[::2]) # print every other letter in the string
print(mystr[::3]) # print every 3rd letter in the string
print(mystr[2:7:2]) # print from index 2 - 7 but print every other string
print(mystr[::-1]) # reverse the string
'''

#real world sceniaro
# lets create a username based off someones first initial and last name utilizing indexing
'''
print('Please enter your first name')
first = input()
print('Please enter your last name')
last = input()

username = first[0] + last[:5]
print('Your new username is ', username)
'''