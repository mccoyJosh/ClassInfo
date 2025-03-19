# a string is simply a list/array of characters placed one after each other
"dog"  # string containing 3 characters
""     # string containing 0 characters, i.e. an empty string. Even


# can use either ", ' or '''/"""
"this is the same thing"
'this is the same thing'
"""this is the same thing"""
'''this is the same thing'''


# use the three quote characters for multiline stirngs
print(
'''
this 
is
a
valid
string
'''
)


# technically, all char objects are considered strings in python
var = ''
print(type(var))

var: chr = ''
print(type(var))

print("This is just a string being printed out")  # just a long string

# Each character in a string is at an index starting from 0
print("This is a string"[0])  # getting a single character from a string




# Just like the mathematical operands, there are operators that can applied to strings

# concatenation (adding strings together)
# just put the + operator between two strings:   <str> + <str>
print("Hi " + "bro")

print("Here" + " " + "I" + " " + "am adding a bunch of strings together")

# more helpful when using variables
first_name = "John"
last_name = "Smith"
print(first_name + " " + last_name)


# Replication operator (multiplying strings)

# Just place an * between a string followed by an int: <str> * <int>
print("Z" * 5)  # results in 'ZZZZZ'

print("Z" * 0)  # results in an empty string

print('abc ' * 10)  # works with any size string
