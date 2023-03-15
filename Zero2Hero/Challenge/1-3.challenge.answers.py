'''
Answer these 3 questions.
    What is the value of the expression 4 * (6 + 5)
    What is the value of the expression 4 * 6 + 5 
    What is the value of the expression 4 + 6 * 5

Solution:
'''
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 *5)

'''
What is the type of the result of the expression 3 + 1.5 + 4?

Solution: Float
'''

'''
What would you use to find a number's square root, as well as its square?
Solution: 
'''
import math
print(7 ** 2)
print(math.sqrt(49))

'''
If s = 'hello' give an index command that returns 'e'. Enter your code in the cell below.
Solution: 
'''
s = "hello"
print(s[1])

'''
Now reverse the string 'hello' using slicing.

Solution:
'''
print(s[::-1])

'''
Given the string hello, give two methods of producing the letter 'o' using indexing.

Solution:
'''
print(s[4])
print(s[-1])


'''
Build this list [0,0,0] two separate ways.

Solution:
'''
list = [0,0,0]
print(list)

list = [0] * 3
print(list)

'''
Reassign 'hello' in this nested list to say 'goodbye' instead: list3 = [1,2,[3,4,'hello']].

Solution:
'''
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

#or

list3 = [1,2,[3,4,'hello']]
list3[2] = [3,4,'goodbye']
print(list3)

#or 

list3 = [1,2,[3,4,'hello']]
list3[2].pop(2)
list3[2].append('goodbye')
print(list3)

'''
Sort the list: list4 = [5,3,2,4,6,1]

Solution:
'''
list4 = [5,3,2,4,6,1]
list4.sort()
print(list4)
