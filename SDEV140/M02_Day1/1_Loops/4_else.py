
# While loops and For loops can both have 'else' statements
# The else statement only activates if the for/while loop exits normally
# So, for instance, if a loop ends unnaturally from a break, then,
# it WON'T execute the else statement
# So, if we wanted to be warned that we didn't find 535 in our list, we can add and else statement to our loop

x = [100, 200, 3235, 652, 232, 21, 535]

for index, element in enumerate(x):
    if element == 535:
        print("I found 535 at: ", index)
        break
else:
    print("I did not find 535")


