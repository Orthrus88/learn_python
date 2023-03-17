'''
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a != b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
'''

2 == 2
2 == 1

'hello' == 'bye'
'Hello' == 'hello'

'2' == 2

2.0 == 2


3 != 3
4 != 3


2 > 1
2 > 3


2 < 4
2 < 1


2 >= 2
4 <= 1


# Compare more than one at a time
# Logical Operators and, or, not

1 < 2 and 2 < 3
1 < 2 < 3

1 < 2 > 3

'h' == 'h' and 2 == 2


1 == 1 or 2 == 2

1 == 1 or 2 == 3

1 == 2 or 2 == 2


not(1 == 1)

not 1 == 1

not 100 > 1000