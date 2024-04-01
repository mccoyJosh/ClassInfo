# In many circumstances, you will need to format your strings so the data being presented can be more easily read
# For instance, lets say we were printing out a chart of data
l = [(0, 122), (1, 21), (2, 325), (3, 0), (10, 2444), (11, 223)]

print("| ID | Number of hours |")
for e_id, hours in l:
    print("| ", id, " | ", hours, " |", sep="")
# When this prints out, it looks bad
# Only if there was some way to make the data appear uniform... oh wait there is!

print()

# F O R M A T T I N G    S T R I N G S
# Formatting strings allows us to convert our data to strings for a better formatting experience
# General format:
'''
<format string> % <data being formatted>
'''
# and if you have multiple data values, you can do this:
'''
<formatting strings> % ( <data-1>, ..., <data-n> )
'''

# For instance, one common formatting tool is being rounding floating point values
float_val = 10.23525
print('Val: %.2f' % float_val)
# If we just look through this example formatting string, we can gather a lot of the aspects of a formatting string

# first off, the string is essentially a normal string until the % sign. This tells python
# that a data will need to be formatted at this place in the string

# The last char of the format, which is 'f' in this instance, tells python it will be formatting a floating point value
# if we used 's', it would interpret it as a string
# if we used 'd', it would interpret is as an integer (it is 'd' instead of 'i' because it represents the word decimal)

# Now, since this is an integer, the .2 means that, following the decimal point, we only want 2 values
# This will round the number provided to the second decimal value

# We end up with the code printing out: Val: 10.24


# Now if we change just one character, the 'f' to an 's', we get a very different print statement:
float_val = 10.23525
print('Val: %.2s' % float_val)
# This prints out Val: 10

# With this same value now being interpreted as a string, instead of rounding to the second decimal place
# (because strings don't have decimal places), it instead does what a .2 means for a string-type formatting string
# What it means is to limit the size of the string to the length of whatever is after the decimal
# SO, it limits 10.23525 to its first two characters, 10

# This is more easily seen when we just use an actual string for this job
x = 'doggo'
print('Val: %.2s' % x)
# This prints out Val: do


# Another function of a formatting string is to ensure that a string is a minimum number of characters
# For instance, if we wanted to print out a bunch of numbers and to make sure the all appear in-line, we can use this
# functionality. All you need to do is put a number to represent the length after the %
val1 = 3
for i in range(10):
    print('Val: %6d' % (val1 ** i))
# To ensure the string is the desired length, python will fill in the other spaces with
# just adding a number, it will put these spaces before the item being formatted, but,
# you can instruct python to put it AFTER the formatted item with using a - sign
val1 = 3
for i in range(10):
    print('Val: %-6d ||' % (val1 ** i))


'''
FOR MORE ON THE SPECIFICS OF FORMAT STRINGS, SEE THIS CHEAT SHEET:
https://learnpython.com/blog/python-string-formatting/
'''

#  Now we can fix our chart
print("| ID | Number of hours |")
for e_id, hours in l:
    print("| ", "%2s" % e_id, " | ", "%-15s" % hours, " |", sep="")





