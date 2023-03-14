# Working with Dictionaries
'''
In dictionaries we can get values without knowing where the value is in the dictionary be calling the list
'''
myDict = {'key1':'value1','key2':'value2'}
print(myDict['key1'])


# Real World?
price_lookup = {'apple':2.99,'oranges':1.99,'milk':4.80}
print(price_lookup['apple'])


# Dicts are flexable in what info they can hold
'''
in the below example we have 
key1 = k1 that holds a value of 123
key2 = k2 that holds a list of numbers 0, 1, and 2
key3 = k3 that holds another dictionary inside with key1 = 'insideKey' and the value of int 100
'''
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
print(d['k1']) # prints 123
print(d['k2']) # prints the list [0, 1, 2]
print(d['k3']) # prints the dict in k3 {'insideKey': 100}


# How do we get shit out of a list or another dictionary that is already inside a dictionary?
# like this
'''
In the below example we are getting the k2 key in the var 'd'
Next we tell it what index we would like to get out of 'k2'
'''
print(d['k2'][1]) # prints the value at index 1 of the list inside the key k2
# That works for getting a list out but how do we remove the dict from a dict
# By calling the key in the dict of course
print(d['k3']['insideKey']) # prints 100 or the value of insideKey inside the key of k3


# assing key values to vars
# We can also assign the key value to a variable
# here we can assign a new var with the value of 123 from the value of key K1
mynum = d['k1']
print(mynum)
# here we can assign the list in k2 to a var that contains the list
mylist = d['k2']
print(mylist)
# here we can even create a new dictionary out of the nested dictionary that is stored in k3
newdict = d['k3']
print(newdict)


# modifying in one line
# First let's reassign the value of the k2 key to be a list of strings
d['k2'] = ['a', 'b', 'c']
print(d)
#next let's call the .upper() function we learned in a previous episode on k2 at the index of 0 to make 'a' 'A'
d['k2'][0].upper()
print(d)

#Why didn't that work... Well if you remember this isn't an inline function so we would need to assign it as it returns a value
d['k2'][0] = d['k2'][0].upper()
print(d)


# that's great but what if we want to build on to a dictionary that already in place
# reassign var d to new dictionary
d = {'k1':100, 'k2':200}
print(d)
# now we have reassgned it let's add a new key of k3 and a value of 300
d['k3'] = 300
print(d)
# how do we modify the value of an existing key?
d['k1'] = 'New Value'
print(d)


# what if I don't know the key names?
print(d.keys())
# what if I want just all the values?
print(d.values())
# what if I want everything
print(d.items())
# note that both keys(), valuse(), and items() are functions and will require the ()


