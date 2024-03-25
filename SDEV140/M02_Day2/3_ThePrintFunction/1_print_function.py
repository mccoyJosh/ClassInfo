# As you know, the print statement writes any text/string to the screen
print("Hello")


#  Print statement will automatically convert non-string values to stirngs (if it can)
# Prints out 10 no problem
print(10)
# Equivalent to:
print(str(10))


# Even for custom-made objects, python will ATTEMPT to convert it to a string
class example_class1:
    def __init__(self):
        pass


example_class = example_class1()
print(example_class)


# But if you add a __str__ method to the object, it should use whatever you define within it as the string
class example_class2:
    def __init__(self):
        pass

    def __str__(self):
        return "This is an example class"


example_class = example_class2()
print(str(example_class))


#  I don't know if you have noticed, but every time you do a print statement, it ends with printing a new line
print('Line 1')
print('Line 2')

#  Without any text it will just print a new line
print("Line 1")
print()
print("Line 3")

# But, you have the option to change that! It doesn't have to be a new line
# This would print out a new line at the END like normal
print("Whatever you wanted to print out")
# But to change the END, add another parameter called end
print("Whatever you wanted to print out", end='!')
print("Whatever you wanted to print out", end='')
print("Whatever you wanted to print out", end='<THIS IS THE NEW END>')


# EXAMPLE
# Common usage of this is if you want to print multiple things out on the same line
print("Hello", end=' ')
print('World')


# If you are making an application where it takes a bit of time to do a process,
# but don't want the user to think it's not doing anything, you can add a progress bar
import time
print('Progress: ', end='')
# Do something
time.sleep(1)
print('.', end='')
# Do something
time.sleep(1)
print('.', end='')
# Do something
time.sleep(1)
print('.', end='')
# Do something
time.sleep(1)
print('.', end='')
# Do something
time.sleep(1)
print('.', end='')
# Do something
print(' DONE')


#  If you have multiple things to string together in your print statement, use commas to print em all out
#  Adding commas automatically separates each item by a space
first_value = 80
second_value = 120

print("The first values is", first_value, "and the second values is", second_value)
# Notice how you didn't need to end the string with spaces because the commas adds it itself


#  Now, the commas are considered "separators" and the default value that python uses to put in their places is a space
#  You can change that though!
print("I", "Have", "Some", "Text", "To", "Print", "!")

print("I", "Have", "Some", "Text", "To", "Print", "!", sep='*')

#  It can be nothing
print("I", "Have", "Some", "Text", "To", "Print", "!", sep='')

# OR however long of a string you would like
print("I", "Have", "Some", "Text", "To", "Print", "!", sep='<SPACE>')


# EXAMPLE
val1 = 10
val2 = 20
val3 = 30
print(val1, val2, val3, sep=' + ', end=' = ')
summation = val1 + val2 + val3
print(summation)

