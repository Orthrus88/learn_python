'''
REVIEW
'''

# Use for, .split(), and if to create a statemtn that will print out words that start with 's':
mystring = 'Print only the words that start with s in this sentence'

mylist = mystring.split()
#print(mylist)

for x in mylist:
    if x[0] == 's':
        print(x)

# Use range() to print all the even numbers from 0 to 10

print(range(0,11))

# Use a list comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
mylist1 = [x for x in range(1,51) if x % 3 == 0]
print(mylist1)

# Go through the string below and if the length of a word is even print "even!"
mystring = 'Print every word in this sentence that has an even number of letters'

mylist = mystring.split()
for x in mylist:
    if len(x) % 2 == 0:
        print('even!')

# Write a program that prints the integers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For multiples of five print "Buzz" instead of the number
# For multiples of both three and five print "FizzBuzz"

mylist = range(1,101)

for x in mylist:
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

# Use list comprehension to create a list of the first letters of every word in the string below
mystring = 'Create a list of the first letters of every word in this string'

mylist = [x[0] for x in mystring.split()]
print(mylist)

