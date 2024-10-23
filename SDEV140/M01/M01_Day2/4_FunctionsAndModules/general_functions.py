# we have already seen a few functions up to this point
# the print function is one example and a good place to start
print("HEY")

# From it we can notice a common thread throughout many functions:
# its structure, that being, usually a word followed by ()

print()

# we can also see with print the idea of a parameter, that being the "thing" we give to it
# in the case of print(), the parameter is the items we give it between its () (parenthesis)

print("parameters :/")

#################################################################################
#################################################################################

# Another very important function is input()
# This gives us the ability to ask the user of our program for some information

# Input is going to be out first example of a function that "returns" something
# In its case, it returns a string of whatever the user typed

# In this example, we capture that returning value in the variable 'name'
# and use it to print out

name = input("Hey, please type in your name: ")
print('Your name is "' + name + '"')


#################################################################################
#################################################################################

# Sometimes we need to get things other than strings from the user though,
# in that case, we still use the input() method, BUT, we need to convert the values to our
# needed format.

# SO WE USING CASTING! int() and float(), for instance

# (These are also functions btw)

age = int(input("Hey, please type in your age: "))
print('If you were 10 years older, you would be: ', (age + 10))

# If we did not convert the string to an integer, this would result in an error!


#################################################################################
#################################################################################

# There are more helpful functions that help show some returning values along with parameters

len("dog") # returns an integer of the length of the string
'hhhh dog'.count('h') # returns an integer of the number of h's that appear in the stirng


