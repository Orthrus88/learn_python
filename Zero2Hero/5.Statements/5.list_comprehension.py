'''
list comprehensions are a unique way of quickly creating a list with python
Good alternative to for loops that use .append()
'''

mystring = 'hello'

#make a list with every character that's in mystring
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)

# let's breakdown the for loop

mylist1 = [letter for letter in mystring]
print(mylist1)

mylist2 = [ x for x in 'word']
print(mylist2)


# Real World
mynumlist = [x for x in range(0,11)]
print(mynumlist)

# We can start performing functions on the first x in the above statement

mynumlist2 = [x**2 for x in range(0,11)]
print(mynumlist2)

# If this is to much for your brain just use for loops and don't worry about computational time

# Lets do it with an if statement
# Lets print out only even numbers
mylist3 = [x for x in range(0,11) if x%2==0]
print(mylist3)

# REAL WORLD
celcius = [0,10,20,34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)