'''
Sets are unordered collections of unique elements
What does this mean?
Sets can only be one representative of the same object so you can't have the number 7 in there more than once or the letter 'z' in there more than once
A set is a collection which is unordered, unchangeable*, and unindexed
'''

# let's assign a var as a set
myset = set()
print(type(myset))

# Let's add an object to the set
myset.add(1)
print(myset) # note that it uses {} but this is not a dictionary as there is no key:value pairs. It is simply a value and nothing more

#add another object
myset.add(2)
print(myset)

# lets add 2 one more time
myset.add(2)
print(myset) # notice there is still only 1, 2 and not 1, 2, 2. This is the value of a set()


'''
REAL WORLD?
'''
# Lets create a list of valuse
mylist = [1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4]
# now let's cast this to a set
print(set(mylist)) # notice this only returns the unique values of a list

# That's great for numbers but does it work on strings?
mylist = ['a','a','b','b','c','c']
print(set(mylist))

# note that a and A are NOT the same so if I had a list of names and had jane and Jane; jane would appear twice in my list. Once as jane and another time as Jane.
mylist = ['a','a','b','b','c','c', 'A', 'A']
print(set(mylist))

# NOTE that you might not have the same output as show as sets are inherently 'unordered' 