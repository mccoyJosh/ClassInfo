# How python determines whether things are true or false

# Keywords in python for both boolean literal types
True
False

print(type(True))  # bool

# At the very lowest layer this is stored as binary (technically)
# As a bool, there are only two options, True, or False
# Therefore, the computer really just knows these variable as False being 0 and True being 1
# We can even see this in converting these bools to numbers:

print(int(True)) # -> results in 1

######################################################################
######################################################################

# Most times, we are not explicitly using the words True or False in our code,
# Rather, we are using EXPRESSIONS which evaluates to either true or false

# All an expression is IS SOMETHING THAT EVALUATES TO A SINGULAR TYPE/VALUE
# THE BOOK DEFINES EXPRESSION AS "A description of a computation that produces a value"

True # This is an expression

"Hey" # This is an expression

1 + 1 # This is an expression

val = 1 + 1 # THIS IS A FULL ON STATEMENT WHICH INCLUDES AN EXPRESSION

######################################################################
######################################################################

# We can see there how boolean can result from "larger" expressions

print(1 == 1)  # evaluates to True and prints it out
print(1 == 0)  # evaluates to False and print it out
print(1 > 0)   # evaluates to True

# In these examples, we can see the first appearances of boolean OPERATORS
# All an operator is IS TYPICALLY A SYMBOL WHICH APPLIES SOME SORT OF OPERATION ONE VALUES

# we see a few here, those being == and > (or <)
# == compares two values and results in True if they are the same value, false otherwise
# > is the greater than operators and will return true if the left operand is greater than the right operand, and false otherwise
# (vice versa for <)

