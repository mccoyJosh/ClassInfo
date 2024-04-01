# There are also cases where you may need to see if a variable equals a number of other values
# You could use an  if-elif-else statement to determine whether the variable is whatever one of the
# values you are checking for, but there is a tool called the match statement which makes checking
# variables more readable

'''
match <variable>:
    case <pattern-1>:
        <instruction>
    .
    .
    case <pattern-n>:
        <instruction>
    case _:
        <default>
'''


# Let's say we are trying to determine the month based off of a number. Again,
# we could use a long list if elif else statements to connect the number to
# it's corresponding month, OR we could use a match statement:

month_num = int(input("Enter the month number: "))

match month_num:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Error: Invalid Month")

# NOTE: if your version of python is not updated past version 3.9, match statements do not work



