'''
Iterations for everyone
'''

mylist = [1,2,3]

for x in mylist:
    print(x)


# use of range function
mylist = [1,2,3,4,5,6,7,8,9,10]

for n in mylist:
    print(n)


# print 'hello' for every item in the list
for num in mylist:
    print('hello')


# Print even numbers else print 'odd'
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'{num} is odd')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)


mystring = 'Hello World'
for letter in mystring:
    print(letter)


tup = (1,2,3)
for x in tup:
    print(x)


# tuple unpacking
mylist = [(1,2,3), (4,5,6), (7,8,9)]

for t in mylist:
    print(t)

for (a,b,c) in mylist:
    print(b)


# dictionaries
d = {'k1':1, 'k2':2, 'k3':3}

for item in d:
    print(item)

# Get items from dictionaries
for item in d.items():
    print(item)

# Get values of keys only
for val in d.values():
    print(val)

