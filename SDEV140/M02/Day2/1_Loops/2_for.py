# Let's say, we wanted to print the ascii value for every letter in a string:

# does this contain
str = "Bababooey!!!\n"


i = 0
while i < len(str):
    char = str[i]
    print(ord(char))
    i = i + 1


# This works, but there is an easier way to do this!
# Using a for loop

# For loop general use:
'''
for <item> in <sequence>:
    <statement-1>
    .
    .
    <statement-n>
'''

# We can simplify the previous example with a for loop
for char in str:
    print(ord(char))


# For loops will repeat as long as there is another item to go through
example_list = ["One", "Two", "Three"]
for element in example_list:
    print(element)
# Once it has printed 3, it has gone through all the items in the list and is done


# The 'in' key word will make it so that every item in a list can be matched to a variable, even for MORE THAN 1 VALUE
big_example_list = [
    ("One", 1),
    ("Two", 2),
    ("Three", 3)
]
for i1, i2 in big_example_list:
    print(i1, " | ", i2)


# RANGE FUNCTION
# Maybe you need to do a certain task a specific number of times.
# That's when you use the for loop with the range keyword!
'''
for <variable> in range(<integer>):
    <statement-1>
    .
    .
    <statement-n>
'''

# Range will create a sequence to a given value, EXCLUSIVE
for i in range(10):
    print(i)
# So this loop will print 0 to 9

# Although, this is still 10 times total, so if you are attempting to do an instruction a certain number of times,
# range(#) should work just fine
for i in range(10):
    print("Hello World")


# EXAMPLE:
# Finding exponent
# n^x = value
n = 2
x = 10
value = 1

for i in range(x):
    value = value * n

print(n, '^', x, '=', value)


# The way the range function works is by making a sequence, and the for loop
var = range(5)
print(var[4])
# Note: this isn't a list and attempting to print 'var' out will just give you 'range(0,5)'
print(var)


# The range function has more functionality!
# You can tell the range function to begin at other values instead of 1, INCLUSIVE
for i in range(5, 10):
    print(i)
# This prints out 5, 6, 7, 8, 9


# Off-by-one Error
# It is a common error to incorrectly identify when a loop ends, generally by 1 unit
# Typically, this happens because loops and specifically the range function works by
# being exclusive of the final value
# for example:
for count in range(1, 4):
    print(count)
# folks MAY think this prints out 1, 2, 3, 4, BUT, since 4 is exclusive, it doesn't include it and the count
# ends up being off  by 1


# Also, by default, the range function goes up 1 value at a time, BUT,
# you can change the step value by adding a 3rd parameter
for i in range(0, 10, 2):
    print(i)

# This can also go backwards! WOW
for i in range(20, 10, -2):
    print(i)


#  ENUMERATE FUNCTION
# Sometimes, along with going through a list of objects, it is helpful to know the index of said item
# The enumerate function will assign an index to all the values in a provided list
example_list = ['x', 'y', 'z']
for i, element in enumerate(example_list):
    print("Index: ", i, " is ", element)


# EXAMPLE:
# Let's say you need to find the index of something in a list
x = [100, 200, 535, 3235, 652, 232, 535, 21, 535]
# WHERE IS 535
for index, element in enumerate(x):
    if element == 535:
        print("I found 535 at: ", index)

# We did not need to create an extra variable to store index ourselves
# (and also increment it every time we were at an index) since
# all that was done for us using enumerate

