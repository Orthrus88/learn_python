'''
Let's get some I/O up in this bitch
'''
# utilizing the open function you want tell python 'with open('file', 'mode')
# we can the use an 'as' statement to be like hey python all that shit I just typed
# can you do that as whatever I'm about to assign you in this case 'z' most people use 'f' but fuck most people
with open('myfile.txt', 'w') as z:
    z.write('Hello this is a text file') # write some bullshit
    z.write('\n') # escape character to create a new line
    z.write('this is the second line') # write somemore bullshit
    z.write('\n')# escape character to create a new line
    z.write('this is the third line') # last line of bullshit... or is it?
    z.close() # good practice to close this dumb ass file

# Now what the fuck does 'w' do? It states we want to write to the file so lets write some more to it
with open('myfile.txt', 'w') as f: # did it as 'f' this time now you fucking happy?
    f.write('This is some more shit to put in here')
    f.close()

# now if you look at your file you will notice there is only one line of text... 
# where did all your other stuff go... you worte over it... Now it's gone forever... hope it wasn't important.
# Now lets append the file to add some more lines
with open('myfile.txt','a') as f: # we will use the 'a' now for the 'mode' section to signify we want to append the file
    f.write('\n') # lets make a new line then put some shit in
    f.write("I'm sorry that I suck at python") # Good that's what I thought.
    f.close()

# Now we get our expected result. Sometimes you have to fail in order to learn... but man do you fail a lot.


# Assigning your file to a var
myfile = open('myfile.txt')
# Now how do we read the file? With .read() you idiot
print(myfile.read())
print(myfile.read()) # now we gett an empty string but why?
# lets imagine there is an invisible cursor and when you read the file that cursor stays at the the bottom of the file. 
# To 'reset' this we need to seek that cursor back to the beginning of the file
myfile.seek(0)
print(myfile.read()) # now this will return the correct information that we expect
# read lines function
myfile.seek(0)
print(myfile.readlines()) # do you notice anything different about the readlines output? 
# ['This is some more shit to put in here\n', "I'm sorry that I suck at python"] 
# it looks like a list and what can we do with lists... use the index and lists are mutable.
myfile.seek(0)
print(myfile.readlines()[1]) # here we will print the item at index 1 as that is the only item that really matters for you

# How to open other files not in your project
'''
All you need to do is type the full file path
Windows users... git gud scrub and type the following
myfile = open("C:\\Path\\To\\File\\myfile.txt") # escape characters are needed 
Linux and also Mac I guess...
myfile = open("/Path/To/My/File/myfile.txt")
'''

'''
Best practices...
Close your fucking files when you are done
Dont give write permissions unless needed if you need to just read a file you can use the following
with open('myfile.txt', 'r') as f:  <-- we use 'r' to read the file
'''