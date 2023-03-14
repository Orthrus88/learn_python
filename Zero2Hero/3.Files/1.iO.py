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

# Now we get our expected result. Sometimes you have to fail in order to learn... but man do you fail a lot.