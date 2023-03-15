# number list
mylist = [1,2,3]
print(mylist)
#Another way to make a list
numlist = [0]*3
print(numlist)

# mixed data types
mylist = ["STRING",100,23.2]
print(mylist)

# Get number of elements in list
print(len(mylist))

# Indexing with lists
mylist = ['one', 'two', 'three']
print(mylist[0])


# slicing with lists
print(mylist[1:])


# Concatonate lists
mylist1 = ['one', 'two', 'three']
mylist2 = ['four', 'five', 'six']
newlist = mylist1 + mylist2
print(newlist)

# lists are mutable objects and can be changed
newlist[0] = 'ONE'
print(newlist)

#appending lists
newlist.append('seven')
print(newlist)

# removing end element from list
newlist.pop()
print(newlist)

# saving a pop to a var
popped_item = newlist.pop()
print(popped_item)

# passing index to pop
newlist.pop(0)
print(newlist)


# Sorting lists. NOTE: .sort is an inplace function and does not return anything. You can not assign to var.
newlist = ['a', 'e', 'x', 'b', 'c']
numlist = [4,1,8,3]
newlist.sort()
numlist.sort()
print(newlist)
print(numlist)

# Example .sort being an inplace function
inplace = [7,5,1,6,8]
sortedlist = inplace.sort()
print(sortedlist) # this will return None as it is a none type since .sort is an inplace function

# reversing lists
numlist.reverse()
print(numlist)
newlist.reverse()
print(newlist)