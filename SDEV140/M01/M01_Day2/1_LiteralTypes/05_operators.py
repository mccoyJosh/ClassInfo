# EXPRESSIONS
# Expression: a set of code which can be evaluated to a value
# DO NOT CONFUSE THIS WITH STATEMENTS
# Statement: An instruction to perform an action; typically a single line of code in python.
#            Statements can consist of expression(s)!


# If integers and floating point values were just here to be represented, that would be cool, but not super helpful
# That's why we have operators!

# Addition
1 + 1      # = 2
-10 + 20   # = 10
1.5 + 1.5  # = 3.0
1.0 + 1    # = 2.0

# Not sure why you would do this, but THIS does work:
True + 1   # = 2

# IF YOU ADD AN INT WITH A FLOAT, THE RESULT WILL ALWAYS BE A FLOATING POINT VALUE. SAME THING FOR ALL BINARY OPERATORS!



# Subtraction
1 - 1      # = 0
-10 - 20   # = -30
4.5 - 1.5  # = 3.0
1.0 - 1    # = 0.0



# Mulitplication
1 * 2          # = 2
2 * 0          # = 0
4.0 * 4        # = 16.0
.235 * 7.4566  # = 1.7523009999999999


# Exponents
1 ** 2      # = 1^2 = 1
2 ** 3      # = 2^3 = 8
4.5 ** 2.5  # = 42.95673695708276
2 ** -1     # = 0.5



# Division (THIS WILL ALWAYS RESULT IN FLOATING POINT VALUES)
1 / 1         # = 1.0
25 / 5        # = 5.0
35.0  / 4.0   # = 8.75
#5 / 0         # = AN ERROR



# Integer Division
# This truncates then result of the division to the nearest whole number, even for floating point values
8 // 3        # = 2
10.3435 // 3   # = 3.0


# Modulo (Remainder) Operator
# Gives the remainder that would result from the division of the two numbers
7 % 3         # = 1
10.3435 % 3   # = 1.3435000000000006

# THIS IS SUPER HELPFUL FOR DETERMINING IF A NUMBER IS EVEN BTW!!!!!!!
# i.e. (<num> % 2) == 0   -> if this is True, then it is even!!!!






# BOOLEAN OPERATORS
# this applies just for boolean type values. Should seem familiar from SDEV 120


# not
# inverses the boolean value
not True      # = False
not False     # = True
not (1 == 1)  # = False


# and
# ensures both are true to result in true
True and True    # = True
True and False   # = False
False and False  # = False

val = 10
(val > 0) and (val < 20)  # = True


# or
# ensures atleast one is true to result in true
True or True    # = True
True or False   # = True
False or False  # = False

val = 1
(val == 0) or (val == 1)  # = True




# Bitwise Operators
print(bin(0B001100))
print(bin(0B001100>>2))
print(bin(0B001100<<2))



# PYTHON IS A STRONGLY TYPED LANGUAGE
# before applying operators to operands, it ensure it is allowed to do that, and if not, it reuslts in an erro
# These all results in errors due to this:
# 1 + "dog"
# "hey" / "soul sister"
# -"dog"
#ord(1)
#chr('x')



# Look up and show operator precedence!!!!


