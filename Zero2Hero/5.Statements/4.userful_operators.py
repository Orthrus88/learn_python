'''
Things that didn't fit well elsewhere
'''
#RANGE
mylist = [1,2,3]

for num in range(10):
    print(num) # prints 0 - 9

for num in range(3,10):
    print(num)

for num in range(0,11,2):
    print(num)

# to pass this a a list type it must be cast that way

mylist = range(1,11)
print(type(mylist))
print(mylist)

mylist = list(range(1,11))
print(type(mylist))
print(mylist)


#ENUMERATE
count = 0
for letter in 'abcde':
    print(f'At index {count} the letter is {letter}')
    count += 1
# more than one way to skin a cat
index = 0
word = 'whatever'
for letter in word:
    print(word[index])
    index += 1
# time to actually use enumerate
for x in enumerate(word):
    print(x)
# notcie that enumerate prints out in tuple format
for ind, let in enumerate(word):
    print(ind)
    print(let)
    print('\n')


#ZIP
mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1, mylist2):
    print(item)

mylist3 = [10,20,30,40]
for item in zip(mylist1,mylist2,mylist3):
    print(item)


#IN... are you in yet?
'''
check if something is in a list or other iterable object types
We have seen this 'in' the for loop
for item in x:
We can also do a bool with this
'''
x = 'a' in 'abc'
print(x)

'''
min and max
return lowest and highest value in list
'''


'''
Random...
we need to import the library for random so lets import that now
'''
from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)
# shuffle operates inplace and cannot be assigned to a var


from random import randint
print(randint(0,100))


#Input Function
input('Enter your name')
#Usually you will assign this to a var 
name = input('Enter your name')
#input always returns a string so be sure to cast it to int or float if you need to assign and work with the number
