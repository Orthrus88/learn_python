'''

indexing
h e l l o
0 1 2 3 4

reverse indexing
h  e  l  l  o
0 -4 -3 -2 -1

slicing - sub secion of string
[start:stop:step]

'hello' or
"hello"

double quots when ' is used in a sentence
"I'm going on a run"
'''
print('hello')

print('hello\nworld') # \ is an escape character... n is new line t is tab

len('hello') #len of 5 spaces count toward this count

'''
INDEXING AND SLICING WITH STRINGS
'''
mystr = 'hello world'
# indexing
print(mystr[0]) # print first letter of mystr
print(mystr[-1]) # print last letter of mystr
print(mystr[5]) # print 6th leter of mystr

# slicing
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
STRING PROPERTIES AND METHODS
'''
# imutability can not change Note concatonate or adding together can be done though

name = "Sam"
#Want to change to Pam can not do "name[0] = 'P'"

last_letters = name[1:] # remove the S from Sam
name2 = 'P' + last_letters
print(name2)

letter = 'z'

x = letter * 10 # make 10 z's on the fly
print(x)

x = 'Hello World'
x = x.upper() # Make everything caps
print(x)
x = x.lower() # Make everything lowercase
print(x)
x = 'Hi this is a string'
x = x.split() # Make a list defaulting to speerate by whitespace
print(x)

# Formatting with the .format() function
print('This is a string {}'.format('INSERTED'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick')) # using the index of the .format we can place the vars or strings in the case anywhere we want

# we can also use vars
print('The {q} {b} {f} 2'.format(f='fox', b='brown', q='quick'))

# formatting floats {value:width.precision f}
result = 100/777
print("the result was {r:1.3f}".format(r=result))

# Formatting with f string literal
name = "Bob"
print(f'Helo, his name is {name}')
