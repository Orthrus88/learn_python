'''
Do something while something else is true or false
'''

# Let's set a value for x
x = 0

# Let's do something while x is less than a number
while x < 10:
    print(f'the current value of x is {x}')
    # lets add to x so it doesn't go forever
    x = x + 1
    # x += 1

else:
    print('X is not less than 5')

'''
keywords in loops
break: Breaks out of the current closest enclosing loop
continue: Goes to the top of the closest enclosing loop
pass: does nothing at all
'''

mylist = [1,2,3]

for item in mylist:
    # future function I know I need with some stuff in here with what I want to do
    pass # place holder for now until you know what you want to do


mystring = 'Sammy'
for letter in mystring:
    if letter == 'm':
        continue # go back to the top of this for statement
    print(letter)

for letter in mystring:
    if letter == 'y':
        break # 'break out of this while loop if the letter ever = y
    print(letter)