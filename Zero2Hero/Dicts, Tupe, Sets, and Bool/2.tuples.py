'''
Tuples are very similar to lists however they are immutable
Tuples are defined using () (1,2,3)
'''

# Create the first tuple
t = (1,2,3)
# Let's create a list to compare it to
mylist = [1,2,3]
# let's confirm that they are the tuple and list
print(type(t))
print(type(mylist))
#This will return the class of tuple and list respectivally

# We also have other options similar to our lists like len
print(len(t)) # returns 3 or the number of elements in our tuple
# indexing and slicing in tuples
print(t[0])
print(t[-1])
print(t[1:])


'''
WORKING WITH TUPLE METHODS
'''
# Working with the count method
# First lets reassign t
t = ('a', 'a', 'b')
print(t.count('a')) # returns 2 as there are 2 a's in our tuple

# Working with index method
print(t.index('a')) # this will return the first index in which it encoutners 'a' so while there are 2 a's in our tuple it will only return the first one found.
print(t.index('b'))


'''
HOW IS A TUPLE DIFFERENT FROM A LIST
'''
# let's modify our list at index 0 to be a new valuse
mylist[0] = 5
print(mylist) # prints out 5, 2, 3

# Let's modify the tuple at index 0
# t[0] = 5 # this will return an error as tuples are not mutable 'tuple' object does not support item assignment
# print(t)
'''
Then why use tuples?
tbh... you probably won't very often while learning python... 
However as you progress and start passing around objects in your program that you need to ensure don't change then you can assgin it as a tuple
'''