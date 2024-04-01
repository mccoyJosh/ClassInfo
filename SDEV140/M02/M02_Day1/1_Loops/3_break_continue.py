# Break and continue are both very important keywords for controlling loops


# CONTINUE KEYWORD
# lets say we wanted to do the exact opposite of what we just did, and wanted to print out all the indices which.
# DON'T have 535.

# We could use the continue keyword to skip the rest of the loop body!
# For our instances, this will skip printing out the index for only elements which are 535
# and thus leave us only with the values which don;t equal 535
x = [100, 200, 535, 3235, 652, 232, 535, 21, 535]
for index, element in enumerate(x):
    if element == 535:
        continue
    print('Index without 535: ', index)


# BREAK KEYWORD
# The break statement will stop a loop in its tracks!
# Whenever the break statement is found, the said loop will stop and move on to whatever is after that
# if we take the code we just had, and perhaps JUST wanted to find the first instance of 535,
#  we could add a break statement

for index, element in enumerate(x):
    if element == 535:
        print("I found 535 at: ", index)
        break
# it stops the search once we find 535 and doesn't go through the rest of the list
