#STRING PROPERTIES AND METHODS
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
'''