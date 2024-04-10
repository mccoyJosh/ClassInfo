# Now, python would be very annoying if we had to contain
# All of our information in one file

# But, we can split it up into many files
# One way to do this is through importing and exporting methods

# All this really refers to is the ability to use a method
# that was created in another file


# I believe we may have already utilized this as well!
# Think of the math library for example:
import math

print(math.factorial(10))

# What is happening is that there is some standard python file named
# math which contains the code to execute the functionality of these
# functions which we are importing. So, despite these being defined
# elsewhere, we can run their code

# To import and export, the first step is to make the file
# You want to have the methods you want exported in
# Then, define your methods!
# For example, take a look at the my_math.py file!
# It is just a normal python file with some functions

# Now, to import it, just use its name and put import before it:
"""
import my_math

print(my_math.add_one(10))
"""

# It is quite literally that easy :)
# Now, when it gets a bit difficult is
# when the file may not be in the same folder as the
# one you are in!

# For instance, if you were in the example_1.py file
# Which is one directory out from the directory with my_math.py
# You need to specifically tell python the path to the file

"""
import Day2.my_math as mm

print(mm.add_one(1))
"""

# Also, you acn tell python to import ... as X so that you can use
# the name provided (X) as where you call the methods you want.
# This saves time as you don't need to write Day2.my_math everytime!
